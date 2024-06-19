                                                              Movie Recommendation System
This project is a Movie Recommendation System built using Streamlit, a popular framework for building interactive web applications in Python. The system recommends movies based on a selected movie from a dropdown list. The recommendations are displayed along with their respective posters.

                                                                    Features
Interactive user interface built with Streamlit.
Dropdown selection of movies for personalized recommendations.
Displays recommended movies along with their posters.
Custom styling for an enhanced user experience.

                                                                Project Structure
The project consists of the following files and directories:

movies_list.pkl: A pickle file containing the list of movies.
similarity.pkl: A pickle file containing the similarity matrix.
posters/: A directory containing local movie poster images.
app.py: The main Python script that runs the Streamlit app.

                                                              How to Run the Project
             Prerequisites:
Python 3.6 or higher
Streamlit
PIL (Pillow)
Pickle

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/saniyaahemad12/movie-recommendation-system.git
cd movie-recommendation-system
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Running the App
To run the Streamlit app, execute the following command:

bash
Copy code
streamlit run app.py
This will start a local web server and open the app in your default web browser.

                                                                     Usage
Select a movie from the dropdown menu on the sidebar.
Click the "Show Recommended Movies" button.
The app will display the recommended movies along with their posters.
Custom Styling
The app includes custom CSS for enhanced styling. This can be found in the st.markdown section of the app.py file.

                                                                Poster Images
The posters/ directory should contain movie poster images named with their respective movie IDs (e.g., 123.jpg). If a poster is not found, a placeholder image is displayed.

                                                                 Contributing
Contributions are welcome! If you have any ideas, suggestions, or issues, please open a pull request or issue on GitHub.
