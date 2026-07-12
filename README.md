)
🎬 AI Reels Generator
📖 Overview

AI Reels Generator is a web application built using Python and Flask that automates the process of creating short reels. Users can upload images, videos, and text. The application converts the text into speech using the ElevenLabs Text-to-Speech API, combines the uploaded media with the generated audio using FFmpeg, and produces a final reel that is displayed in the gallery.

🚀 Features
📤 Upload images and videos
📝 Convert text into natural speech using ElevenLabs API
🎥 Generate reels automatically with FFmpeg
🆔 Unique file management using UUID
📁 Secure file upload and storage
🖼️ Gallery section to view generated reels
⚠️ Error handling for invalid uploads and processing failures
🌐 Simple and user-friendly interface
🛠️ Tech Stack
Backend
Python
Flask
Frontend
HTML
CSS
Bootstrap
Database
SQLite / MySQL (use whichever your project actually uses)
APIs & Tools
ElevenLabs API
FFmpeg
UUID
Version Control
Git
GitHub
📂 Project Workflow
User Uploads Image/Video + Text
            │
            ▼
      Flask Backend
            │
            ▼
Generate Unique Folder using UUID
            │
            ▼
Convert Text to Speech (ElevenLabs API)
            │
            ▼
Merge Media + Audio using FFmpeg
            │
            ▼
Generate Final Reel
            │
            ▼
Display Reel in Gallery
🎯 Key Learnings

During this project, I gained hands-on experience in:

Flask Backend Development
REST API Integration
File Handling in Python
UUID-based File Management
FFmpeg Media Processing
Error Handling & Debugging
Project Structure & Organization
🔮 Future Improvements
User Authentication
Background Music Support
AI Caption Generation
Multiple Video Templates
Cloud Storage Integration
Download & Share Options
👨‍💻 Author

Rahul Mandloi

Python Backend Developer
Passionate about Backend Development and Problem Solving
