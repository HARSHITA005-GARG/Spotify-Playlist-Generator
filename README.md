# 🎵 **Spotify Mood Playlist Generator**  

Effortlessly generate personalized Spotify playlists based on your mood using this Python-powered web application. The app integrates with the Spotify API to recommend tracks and create customized playlists.  

---

## 🚀 **Features**  

- **Spotify Authentication**: Securely log in using OAuth 2.0.  
- **Mood-Based Recommendations**: Generate playlists based on your mood (e.g., happy, sad, energetic).  
- **Personalized Playlists**: Create and save playlists directly to your Spotify account.  
- **User-Friendly Interface**: Built with Streamlit for an interactive experience.  

---
## 🛠 **Tech Stack**  

- **Python**  
- **Spotipy (Spotify API Wrapper)**  
- **Streamlit**  
- **Spotify API**  

---

## 📦 **Installation**  

Follow these steps to set up and run the app:  

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/HARSHITA005-GARG/Spotify-Playlist-Generator.git
    cd Spotify-Playlist-Generator
    ```

2. **Create and Activate Virtual Environment**  
    ```bash
    python -m venv env
    ```
    **Activate Environment**  
    - On **Windows**:  
      ```bash
      env\Scripts\activate
      ```
    - On **Mac/Linux**:  
      ```bash
      source env/bin/activate
      ```

3. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Spotify API**  
    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)  
    - Create a new app to obtain your **Client ID** and **Client Secret**  
    - Set `http://127.0.0.1:8888/callback` as the Redirect URI  

5. **Create a `.env` File**  
    ```env
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
    ```

---

## 🖥 **Usage**  

1. **Run the Application**  
    ```bash
    streamlit run app.py
    ```

2. **Open in Browser**  
    - Visit: [http://127.0.0.1:8501](http://127.0.0.1:8501)  

3. **Generate Playlist**  
    - Enter your mood (e.g., happy, sad, relaxed).  
    - Click on **Generate Playlist**.  
    - Access your personalized playlist directly on Spotify.  

---

## 🛡 **Troubleshooting**  

- Ensure Spotify API credentials in your `.env` file are correct.  
- Confirm that your redirect URI matches `http://127.0.0.1:8888/callback` in your Spotify Developer Dashboard.  
- Verify the Streamlit app is running on port 8501.  

---

## 🌿 **Contributing**  

Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. Commit your changes (`git commit -m 'Add your feature'`).  
4. Push to your branch (`git push origin feature/your-feature`).  
5. Open a Pull Request.  

---

## 📜 **License**  

This project is licensed under the [MIT License](LICENSE).  

---

## 🌐 **Connect**  

- **GitHub Repository**: [Spotify-Playlist-Generator](https://github.com/HARSHITA005-GARG/Spotify-Playlist-Generator)  
- **Render Deployment**: [View on Render](https://spotify-playlist-generator-f4mr.onrender.com)
- **Streamlit Deployment**: [View on Streamlit](https://spotify-playlist-generator-005.streamlit.app/)  
