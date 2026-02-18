import { useState, useEffect } from "react";
import { vapi, startAssistant, stopAssistant } from "./ai";
import ActiveCallDetails from "./call/ActiveCallDetails";

function App() {
  const [started, setStarted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [assistantIsSpeaking, setAssistantIsSpeaking] = useState(false);
  const [volumeLevel, setVolumeLevel] = useState(0);
  const [callId, setCallId] = useState("");
  const [callResult, setCallResult] = useState(null);
  const [loadingResult, setLoadingResult] = useState(false);

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    vapi
      .on("call-start", () => {
        setLoading(false);
        setStarted(true);
      })
      .on("call-end", () => {
        setStarted(false);
        setLoading(false);
      })
      .on("speech-start", () => {
        setAssistantIsSpeaking(true);
      })
      .on("speech-end", () => {
        setAssistantIsSpeaking(false);
      })
      .on("volume-level", (level) => {
        setVolumeLevel(level);
      });
  }, []);

  const handleInputChange = (setter) => (event) => {
    setter(event.target.value);
  };

  const handleStart = async () => {
    setLoading(true);
    const data = await startAssistant(firstName, lastName, email, phoneNumber);
    setCallId(data.id);
  };

  const handleStop = () => {
    stopAssistant();
    getCallDetails();
  };

  const getCallDetails = (interval = 3000) => {
    setLoadingResult(true);
    fetch("/call-details?call_id=" + callId)
      .then((response) => response.json())
      .then((data) => {
        if (data.analysis && data.summary) {
          console.log(data);
          setCallResult(data);
          setLoadingResult(false);
        } else {
          setTimeout(() => getCallDetails(interval), interval);
        }
      })
      .catch((error) => alert(error));
  };

  const showForm = !loading && !started && !loadingResult && !callResult;
  const allFieldsFilled = firstName && lastName && email && phoneNumber;

  return (
    <div className="app-container">
      {showForm && (
        <div className="form-container">
          <h1>Contact Details (Required)</h1>
          <div className="input-group">
            <label htmlFor="firstName" className="input-label">First Name</label>
            <input
              type="text"
              id="firstName"
              placeholder="First Name"
              value={firstName}
              className="input-field"
              onChange={handleInputChange(setFirstName)}
            />
          </div>
          <div className="input-group">
            <label htmlFor="lastName" className="input-label">Last Name</label>
            <input
              type="text"
              id="lastName"
              placeholder="Last Name"
              value={lastName}
              className="input-field"
              onChange={handleInputChange(setLastName)}
            />
          </div>
          <div className="input-group">
            <label htmlFor="email" className="input-label">Email Address</label>
            <input
              type="email"
              id="email"
              placeholder="Email address"
              value={email}
              className="input-field"
              onChange={handleInputChange(setEmail)}
            />
          </div>
          <div className="input-group">
            <label htmlFor="phoneNumber" className="input-label">Phone Number</label>
            <input
              type="tel"
              id="phoneNumber"
              placeholder="Phone number"
              value={phoneNumber}
              className="input-field"
              onChange={handleInputChange(setPhoneNumber)}
            />
          </div>
          {!started && (
            <button
              onClick={handleStart}
              disabled={!allFieldsFilled}
              className="button"
            >
              Call PyMentor
            </button>
          )}
        </div>
      )}
      {loadingResult && <p>Loading call details... please wait</p>}
      {!loadingResult && callResult && (
        <div className="call-result-container">
          <h2>Call Result</h2>
          <p>Qualified: {callResult.analysis.structuredData.is_qualified.toString()}</p>
          <p>{callResult.summary}</p>
        </div>
      )}
      {(loading || loadingResult) && <div className="loading"></div>}
      {started && (
        <ActiveCallDetails
          assistantIsSpeaking={assistantIsSpeaking}
          volumeLevel={volumeLevel}
          endCallCallback={handleStop}
        />
      )}
    </div>
  );
}

export default App;
