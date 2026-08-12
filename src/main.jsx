import { useRef, useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import { cvData } from "./data";
import "./styles.css";

function SectionTitle({ children }) {
  return <h2 className="section-title"><span>{children}</span></h2>;
}

function Card({ children, accent = "blue" }) {
  return <article className={`card card-${accent}`}>{children}</article>;
}

function LinkIcon({ href, children }) {
  return href ? <a href={href} target="_blank" rel="noreferrer">{children}</a> : children;
}

function Resume() {
  const resumeRef = useRef(null);
  const [exporting, setExporting] = useState(false);
  function imprimirCV() {
    window.print();
  }

  return (
    <main className="app-shell">
      <div className="toolbar">
        <button onClick={imprimirCV} disabled={exporting}>
          {exporting ? "Generando PDF..." : "Imprimir CV"}
        </button>
      </div>

      <section className="resume" ref={resumeRef}>
        <header className="hero">
          <img className="portrait" src={cvData.photo} alt={`Foto de ${cvData.name}`} />
          <div className="hero-copy">
            <h1>{cvData.name}</h1>
            <p className="role">{cvData.role}</p>
            <div className="summary">{cvData.summary}</div>
            <div className="contact-row">
              <span>{cvData.location}</span>
              <a href={`mailto:${cvData.email}`}>{cvData.email}</a>
              <span>{cvData.phone}</span>
              <span><strong>GitHub:</strong> <LinkIcon href={cvData.githubUrl}>{cvData.github}</LinkIcon></span>
              <span><strong>LinkedIn:</strong> <LinkIcon href={cvData.linkedinUrl}>{cvData.linkedin}</LinkIcon></span>
            </div>
          </div>
        </header>

        <div className="skill-row">
          {cvData.skills.map((skill) => <span key={skill}>{skill}</span>)}
        </div>

        <div className="columns">
          <div>
            <SectionTitle>Proyectos</SectionTitle>
            {cvData.projects.map((project) => (
              <Card key={project.title}>
                <h3>{project.title}</h3>
                <p className="stack">{project.stack}</p>
                <ul>{project.bullets.map((item) => <li key={item}>{item}</li>)}</ul>
                {project.url && <a className="project-link" href={project.url} target="_blank" rel="noreferrer">Ver repositorio</a>}
              </Card>
            ))}

            <SectionTitle>Formación</SectionTitle>
            {cvData.education.map((item) => (
              <Card key={item.title} accent="gold">
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
              </Card>
            ))}
          </div>

          <div>
            <SectionTitle>Experiencia</SectionTitle>
            {cvData.experience.map((job) => (
              <Card key={job.title} accent="green">
                <h3>{job.title}</h3>
                <p className="stack">{job.period}</p>
                <ul>{job.bullets.map((item) => <li key={item}>{item}</li>)}</ul>
              </Card>
            ))}

              <section className="print-page-break">
                <SectionTitle>Idiomas</SectionTitle>
                <Card accent="purple">
                  <ul>{cvData.languages.map((item) => <li key={item}>{item}</li>)}</ul>
                </Card>

                <SectionTitle>Competencias</SectionTitle>
                <Card accent="purple">
                  <ul>{cvData.strengths.map((item) => <li key={item}>{item}</li>)}</ul>
                </Card>
              </section>
          </div>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<Resume />);
