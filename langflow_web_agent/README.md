# Langflow Web Agent

A powerful web scraping and data extraction tool built with Langflow, leveraging Bright Data's Web Unlocker and Dataset APIs to provide intelligent web data collection capabilities.

## 🌟 Features

- **🔍 SERP Search**: Advanced search engine results page scraping for Google and Bing
- **📱 Reddit Search API**: Comprehensive Reddit post discovery with flexible filtering
- **💬 Reddit Post Retrieval**: Extract detailed comments and metadata from specific Reddit threads
- **⚡ Async Processing**: Efficient concurrent data processing
- **🛡️ Bright Data Integration**: Reliable proxy rotation and anti-bot protection

## 📋 Prerequisites

- Python 3.8+
- Bright Data account with API access
- Valid Bright Data API key

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/dimipash/AI-Python-projects.git
cd AI-Python-projects/langflow_web_agent
```

### 2. Set Up Virtual Environment

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Or using standard venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
# Or: pip install -r requirements.txt
```

### 4. Configure Environment

**Option A: Environment Variable**
```bash
export BRIGHTDATA_API_KEY="your_brightdata_api_key_here"
```

**Option B: `.env` File (Recommended)**
```bash
# Create .env file in project root
echo "BRIGHTDATA_API_KEY=your_brightdata_api_key_here" > .env
```

## 💡 Usage Examples

### SERP Search Operations

```python
from web_operations import serp_search

# Search Google for recent AI developments
google_results = serp_search(
    query="latest AI breakthroughs 2024",
    engine="google",
    num_results=20
)

# Search Bing for programming tutorials
bing_results = serp_search(
    query="Python machine learning tutorial",
    engine="bing",
    num_results=15
)

print(f"Found {len(google_results)} Google results")
print(f"Found {len(bing_results)} Bing results")
```

### Reddit Content Discovery

```python
from web_operations import reddit_search_api

# Find trending AI discussions
ai_posts = reddit_search_api(
    keyword="artificial intelligence",
    sort_by="Hot",
    num_of_posts=100,
    subreddit="MachineLearning"
)

# Search for recent programming questions
dev_posts = reddit_search_api(
    keyword="Python debugging",
    sort_by="New",
    num_of_posts=50,
    time_filter="week"
)
```

### Reddit Thread Analysis

```python
from web_operations import reddit_post_retrieval

# Analyze specific discussions
post_urls = [
    "https://www.reddit.com/r/MachineLearning/comments/xyz123/breakthrough_in_llm_training/",
    "https://www.reddit.com/r/artificial/comments/abc456/future_of_ai_development/"
]

# Extract comprehensive thread data
thread_data = reddit_post_retrieval(
    urls=post_urls,
    days_back=30,
    load_all_replies=True,
    include_metadata=True
)

for thread in thread_data:
    print(f"Thread: {thread['title']}")
    print(f"Comments: {len(thread['comments'])}")
    print(f"Engagement: {thread['upvotes']} upvotes")
```

## 📁 Project Architecture

```
langflow_web_agent/
├── main.py                 # Application entry point and orchestration
├── web_operations.py       # Core web scraping functions
├── snapshot_operations.py  # Bright Data snapshot management
├── prompts.py             # LLM prompt templates
├── requirements.txt       # Python dependencies
├── .env                   # Environment configuration (create this)
└── README.md             # Project documentation
```

### Module Descriptions

- **`main.py`**: Coordinates the entire workflow and handles user interactions
- **`web_operations.py`**: Implements SERP and Reddit scraping functionality
- **`snapshot_operations.py`**: Manages Bright Data API interactions and data polling
- **`prompts.py`**: Contains structured prompts for AI model interactions

## ⚙️ Configuration Options

### SERP Search Parameters

| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| `query` | Search query string | Required | Any string |
| `engine` | Search engine | `"google"` | `"google"`, `"bing"` |
| `num_results` | Maximum results | `10` | `1-100` |
| `region` | Geographic region | `"US"` | ISO country codes |

### Reddit Search Parameters

| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| `keyword` | Search keyword | Required | Any string |
| `sort_by` | Sort order | `"Hot"` | `"Hot"`, `"New"`, `"Top"`, `"Rising"` |
| `num_of_posts` | Number of posts | `25` | `1-1000` |
| `time_filter` | Time range | `"all"` | `"hour"`, `"day"`, `"week"`, `"month"`, `"year"`, `"all"` |
| `subreddit` | Specific subreddit | `None` | Any valid subreddit name |

## 🔧 Troubleshooting

### Common Issues

**API Key Errors**
```bash
# Verify your API key is set correctly
echo $BRIGHTDATA_API_KEY
# Should display your key (first few characters)
```

**Rate Limiting**
- Implement delays between requests
- Use Bright Data's built-in rate limiting features
- Consider upgrading your Bright Data plan for higher limits

**Connection Issues**
- Check your internet connection
- Verify Bright Data service status
- Ensure your IP isn't blocked


## 🙏 Acknowledgments

- [Langflow](https://github.com/logspace-ai/langflow) for the workflow framework
- [Bright Data](https://brightdata.com/) for reliable web scraping infrastructure
- The open-source community for continuous inspiration

---

⭐ **Star this repository if you found it helpful!**