import click
import json
import pickle
from pathlib import Path
from src.loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer
from src.query import DataQuery


DATA_FILE = ".ai_data_analyst.pkl"


def save_state(loader, analyzer, visualizer):
    """Save current session state."""
    with open(DATA_FILE, "wb") as f:
        pickle.dump(
            {"loader": loader, "analyzer": analyzer, "visualizer": visualizer}, f
        )


def load_state():
    """Load previous session state."""
    if not Path(DATA_FILE).exists():
        return None
    with open(DATA_FILE, "rb") as f:
        return pickle.load(f)


@click.group()
def cli():
    """AI Data Analyst - Analyze data with natural language queries."""
    pass


@cli.command()
@click.argument("file_path")
def load(file_path):
    """Load a data file (CSV or Excel)."""
    click.echo(f"Loading {file_path}...")

    loader = DataLoader()
    data = loader.load(file_path)

    analyzer = DataAnalyzer(data)
    visualizer = DataVisualizer(data)

    save_state(loader, analyzer, visualizer)

    info = loader.get_info()
    click.echo(f"\nLoaded successfully!")
    click.echo(f"Rows: {info['rows']}, Columns: {info['columns']}")
    click.echo(f"Columns: {', '.join(info['column_names'])}")


@cli.command()
def info():
    """Show information about loaded data."""
    state = load_state()
    if not state:
        click.echo("No data loaded. Run 'load' first.")
        return

    info = state["loader"].get_info()
    click.echo(json.dumps(info, indent=2))


@cli.command()
def analyze():
    """Analyze all columns and show statistics."""
    state = load_state()
    if not state:
        click.echo("No data loaded. Run 'load' first.")
        return

    summary = state["analyzer"].get_summary()
    click.echo(json.dumps(summary, indent=2))

    click.echo("\n--- Column Statistics ---")
    for col, stats in state["analyzer"].describe_all().items():
        click.echo(f"\n{col}:")
        click.echo(json.dumps(stats, indent=2))


@cli.command()
@click.option("--column", required=True, help="Column name")
def describe(column):
    """Get statistics for a specific column."""
    state = load_state()
    if not state:
        click.echo("No data loaded. Run 'load' first.")
        return

    stats = state["analyzer"].describe_column(column)
    click.echo(json.dumps(stats, indent=2))


@cli.command()
@click.option(
    "--type",
    "plot_type",
    required=True,
    type=click.Choice(["histogram", "bar", "box", "scatter", "correlation"]),
)
@click.option("--column", help="Column name (for histogram, bar, box)")
@click.option("--x", help="X column (for scatter)")
@click.option("--y", help="Y column (for scatter)")
def plot(plot_type, column, x, y):
    """Generate a visualization."""
    state = load_state()
    if not state:
        click.echo("No data loaded. Run 'load' first.")
        return

    viz = state["visualizer"]

    try:
        if plot_type == "histogram":
            path = viz.histogram(column)
        elif plot_type == "bar":
            path = viz.bar_chart(column)
        elif plot_type == "box":
            path = viz.box_plot(column)
        elif plot_type == "scatter":
            path = viz.scatter_plot(x, y)
        elif plot_type == "correlation":
            path = viz.correlation_heatmap()

        click.echo(f"Saved: {path}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument("question")
def query(question):
    """Ask a question about the data in natural language."""
    state = load_state()
    if not state:
        click.echo("No data loaded. Run 'load' first.")
        return

    try:
        q = DataQuery()
        answer = q.ask(question, state["loader"].data)
        click.echo(answer)
    except ValueError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"API Error: {e}")


if __name__ == "__main__":
    cli()
