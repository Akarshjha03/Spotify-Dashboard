# Spotify Power BI Dashboard 🎶📊

Welcome to the **Spotify Power BI Dashboard** repository! This project presents an interactive and dynamic Power BI dashboard that visualizes various Spotify data insights, such as listening habits, popular tracks, artists, genres, and more.

![Dashboard Preview](link-to-dashboard-image)

## 🎯 Project Overview

The Spotify Power BI Dashboard allows users to explore their Spotify data through detailed visualizations, making it easier to understand trends and analyze personal or public listening habits. This project uses the Spotify API to gather real-time data and integrates it into Power BI to create a seamless and informative dashboard.

## 🚀 Features

- **Real-time Data**: Fetches the latest data from Spotify using the Spotify API.
- **Interactive Visualizations**: Dynamic charts and graphs for exploring data.
- **Filter Options**: Filter data based on time range, artists, genres, tracks, and more.
- **Customizable**: Tailor the dashboard to display the metrics you care about.
- **User-Friendly Interface**: Intuitive design for easy navigation and insight discovery.

## 🛠️ Tech Stack

- **Power BI**: For building the interactive dashboard and visualizations.
- **Spotify API**: For fetching real-time data.
- **Power Query**: Used to clean and prepare data for analysis.
  
## 📦 Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/spotify-powerbi-dashboard.git
    cd spotify-powerbi-dashboard
    ```

2. **Set Up Spotify API Credentials**:
    - Create a Spotify developer account [here](https://developer.spotify.com/dashboard/).
    - Create a new app and get your Client ID and Client Secret.
    - Configure API credentials in Power BI or your environment.

3. **Power BI Setup**:
    - Open Power BI Desktop.
    - Import the `Spotify-PowerBI-Dashboard.pbix` file from this repository.
    - Connect your Spotify data using the provided API credentials.

4. **Refresh Data**:
    - Refresh the data to fetch the latest Spotify data from the API.

## 📊 Visualizations

The dashboard includes the following key visualizations:

- **Top Artists**: Visualizes the top artists based on listening time or frequency.
- **Top Tracks**: Displays the most played tracks over a selected time period.
- **Genre Distribution**: Provides an overview of the user's favorite genres.
- **Listening Trends**: Line charts showing listening habits over days, weeks, or months.

## 📝 How to Use

- Navigate through the dashboard to explore different visualizations.
- Use the filter options to customize the view (e.g., select a time range, genre, or artist).
- The dashboard is interactive, allowing you to drill down into specific data points for detailed insights.

## 📂 Project Structure

```bash
spotify-powerbi-dashboard/
├── Spotify-PowerBI-Dashboard.pbix  # Power BI Dashboard file
├── README.md                       # Project documentation
└── assets/                         # Any images or assets used in the README
