import { useEffect } from "react";
import { TextField } from "@mui/material";
import "./ByteCarePage.css";
const ByteCarePage = () => {
  useEffect(() => {
    const scrollAnimElements = document.querySelectorAll(
      "[data-animate-on-scroll]"
    );
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

  return (
    <div className="byte-care-page" data-animate-on-scroll>
      <div className="right-section">
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
            label="Symptom 1"
            size="medium"
            margin="none"
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 2"
            size="medium"
            margin="none"
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 3"
            size="medium"
            margin="none"
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 4"
            size="medium"
            margin="none"
          />
          <TextField
            className="input-symptom-1"
            color="primary"
            variant="outlined"
            type="text"
            label="Symptom 5"
            size="medium"
            margin="none"
          />
        </div>
        <button className="check-result-button">
          <div className="check-result">Check Result</div>
        </button>
        <div className="result-field">
          <div className="result">Result</div>
          <input className="result-container" type="text" />
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
