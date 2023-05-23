import { useEffect, useState } from "react";
import { TextField } from "@mui/material";
import "./ByteCarePage.css";
import React from 'react';

const ByteCarePage = () => {
  
  const [output, setOutput] = useState('');
  const [symptoms, setSymptoms] = useState({
    symptom1: "",
    //symptom2: "",
    //symptom3: "",
    //symptom4: "",
    //symptom5: "",
  });

  const handleSymptomChange = (event, symptomKey) => {
    setSymptoms((prevState) => ({
      ...prevState,
      [symptomKey]: event.target.value,
      
    }));
  };

  const handleClick = () => {
    const queryParams = new URLSearchParams(symptoms).toString();
    fetch(`http://127.0.0.1:5000/randomforest?${queryParams}`, {  
      headers: {
        Accept: 'application/json',
      },
      // Add any necessary request body here
    })
      .then(response => {
        const contentType = response.headers.get('content-type')
        if(!contentType || !contentType.includes('application/json')){
          throw new Error("Invalid content type")
        }
        return response.json()
      })
      .then(data => {
        // Access the result property from the JSON data
        //const result = data.result;
        setOutput(data.result);
        //console.log(result);
      })
      .catch(error => {
        console.log(error);
      });
  };


  useEffect(() => {
    const scrollAnimElements = document.querySelectorAll(
      "[data-animate-on-scroll]"
    );

      //axio


    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting || entry.intersectionRatio > 0) {
            const targetElement = entry.target;
            targetElement.classList.add("animate");
            observer.unobserve(targetElement);
          }
        }
      },
      {
        threshold: 0.15,
      }
    );

    for (let i = 0; i < scrollAnimElements.length; i++) {
      observer.observe(scrollAnimElements[i]);
    }

    return () => {
      for (let i = 0; i < scrollAnimElements.length; i++) {
        observer.unobserve(scrollAnimElements[i]);
      }
    };
  }, []);


  const stringArray = output.split('\n');
  
  return (
    <div className="byte-care-page" data-animate-on-scroll>
      <div className="right-section">
        <div className="wrap">
        <div className="header">
          <span>{`What Is Your `}</span>
          <span className="symtoms">Symtoms?</span>
        </div>
        <div className="symptom-fields">
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptoms"
            size="medium"
            margin="none"
            multiline
            rows={4}
            fullWidth
            value={symptoms.symptom1}
            onChange={(event) => handleSymptomChange(event, "symptom1")}
          />
          {/*<TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 2"
            size="medium"
            margin="none"
            value={symptoms.symptom2}
          onChange={(event) => handleSymptomChange(event, "symptom2")}
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 3"
            size="medium"
            margin="none"
            value={symptoms.symptom3}
            onChange={(event) => handleSymptomChange(event, "symptom3")}
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 4"
            size="medium"
            margin="none"
            value={symptoms.symptom4}
            onChange={(event) => handleSymptomChange(event, "symptom4")}
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 5"
            size="medium"
            margin="none"
            value={symptoms.symptom5}
            onChange={(event) => handleSymptomChange(event, "symptom5")}
          />*/}
        </div>
        <button className="check-result-button" onClick={handleClick}>
          <div className="check-result">Check Result</div>
        </button>
        <div className="result-field">
          <div className="result">Result</div>

              <p className="result-container">
                {stringArray.map((line, index) => {
                  if (line.includes("<b>")) {
                    const parts = line.split("<b>");
                    return (
                      <p key={index}>
                        {parts.map((part, partIndex) => {
                          if (part.includes("</b>")) {
                            const boldParts = part.split("</b>");
                            return (
                              <React.Fragment key={partIndex}>
                                <b>{boldParts[0]}</b>
                                {boldParts[1]}
                              </React.Fragment>
                            );
                          }
                          return part;
                        })}
                      </p>
                    );
                  }
                  return <p key={index}>{line}</p>;
                })}         
              </p>

          </div>
          </div>
        </div>
      <div className="left-section">
        <div className="left-section-content">
          <div className="bytecare">ByteCare.</div>
          <div className="a-disease-predictor">{`A disease predictor that utilizes user input of symptoms to accurately predict potential diseases `}</div>
        </div>
        <img
          className="left-section-image"
          alt=""
          src="/left-section-image@2x.png"
        />
      </div>
    </div>
  );
};

export default ByteCarePage;
