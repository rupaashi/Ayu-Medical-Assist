# Ayu-Medical-Assist
AYU - AI Health Assistant

An AI-driven assistant engineered to enhance the accessibility and comprehension of healthcare information.

🚀 Live Demonstration

The live application is available for review at:
https://ayuhealthassistant.netlify.app/

✨ Project Overview

AYU is a multilingual, voice-interactive web application developed to demystify complex medical information for end-users. Employing a "Blushing Sands" aesthetic, the application is intentionally designed to function as a calming, reassuring, and highly accessible tool, particularly for individuals who may not be technologically proficient.

💡 The Problem Statement

Navigating medical information frequently presents significant challenges, often characterized by complexity, intimidation, and resultant user anxiety. Patients commonly encounter several primary difficulties:

Inability to interpret the specialized terminology and jargon prevalent in medical reports.

Heightened anxiety concerning symptoms, coupled with uncertainty regarding appropriate subsequent actions.

Perception of procedural friction associated with scheduling physician appointments.

Linguistic barriers that impede the effective use of digital health platforms.

🎯 Our Solution

AYU (a name derived from the Hindi word for "life") is a secure, serverless web application architected to address these challenges. It provides users with three core functionalities through an intuitive, conversational interface:

Medical Report Interpretation: Enables users to submit medical reports (either via paste or a provided sample) to receive a simplified, jargon-free explanation of the findings.

Symptom Assessment: Implements a guided, logical triage protocol. The "bot" engages the user in a step-by-step diagnostic questionnaire to help determine a recommended course of action, such as rest, scheduling a non-urgent appointment, or seeking immediate medical care.

Appointment Scheduling: Facilitates a conversational workflow for scheduling medical appointments, culminating in the generation of a Google Calendar integration link.

Bilingual Voice Capabilities: Provides comprehensive support for both English and Hindi (हिन्दी). This is achieved through the integration of the browser's native Web Speech API for both SpeechRecognition (voice-to-text) and SpeechSynthesis (text-to-speech).

🛠 Technical Stack

This project represents a full-stack application constructed utilizing modern, serverless technologies.

Frontend:

HTML5

Tailwind CSS (Utilized for all styling, including the responsive "glassmorphism" user interface)

Web Speech API (Implemented for SpeechRecognition and SpeechSynthesis)

Backend (Serverless):

Netlify Serverless Function (Written in JavaScript/Node.js)

This backend functions as a secure proxy, abstracting and protecting the confidential API key.

👥 The Team

Shravasti Sharma

Rupashi Jain

Shinjini Srivastava
