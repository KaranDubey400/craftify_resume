import streamlit as st



class About_section():
    def About_Section():
        
        st.markdown("<h1 style='color:  #F05A7E;'>About Craftify</h1>", unsafe_allow_html=True)
        st.write("Craftify is an innovative web application revolutionizing the job search experience. By harnessing the power of cutting-edge technologies like Natural Language Processing (NLP) and Machine Learning, Craftify empowers users to craft tailored resumes and discover relevant job opportunities effortlessly.")

        # Key Features
        st.markdown("<h2 style='color:  #F05A7E;'>Key Features:</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:  #F05A7E;'>1 Resume Analyzer (Resume Parser):</h3>", unsafe_allow_html=True)
        st.write("   Craftify's flagship feature, the Resume Analyzer, is a sophisticated tool that parses resumes and job descriptions with precision. Utilizing advanced NLP algorithms, it identifies critical information such as the user's contact details, location, and crucial keywords. By comparing the user's resume with target job descriptions, it provides comprehensive insights into missing keywords and essential hard and soft skills sought by recruiters. Moreover, the built-in ATS Scanner ensures seamless integration with applicant tracking systems, optimizing resume visibility.")
        st.markdown("<h3 style='color:  #F05A7E;'>2. Job Suggestion Searching Platform:</h3>", unsafe_allow_html=True)
        st.write("   Simplifying the job search process, Craftify offers a personalized job suggestion platform. Through intelligent algorithms analyzing user search history and preferences, the platform delivers curated job listings tailored to match the user's interests and qualifications.")
        st.markdown("---")
        # How It Works
        st.markdown("<h2 style='color:  #F05A7E;'>How It Works:</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:  #F05A7E;'>1. Resume Analysis:</h3>", unsafe_allow_html=True)
        st.write("   Users seamlessly upload their resumes and target job descriptions to Craftify. The platform's advanced algorithms conduct a thorough analysis, highlighting areas for alignment and improvement. Through intuitive visualizations and actionable insights, users gain invaluable guidance on optimizing their resumes for specific roles.")
        st.markdown("<h3 style='color:  #F05A7E;'>2. Keyword Implementation:</h3>", unsafe_allow_html=True)
        st.write("   Craftify guides users in strategically implementing essential keywords into their resumes. With tailored recommendations based on industry trends and job requirements, users can enhance their profiles to captivate potential employers. Future updates will further streamline this process, offering step-by-step instructions for seamless keyword integration.")
        st.markdown("<h3 style='color:  #F05A7E;'>3. Job Search Recommendations:</h3>", unsafe_allow_html=True)
        st.write("   Leveraging user preferences and search history, Craftify provides personalized job recommendations. Users receive a curated selection of relevant job openings, saving time and effort in their job hunt. With an intuitive interface and effortless navigation, Craftify simplifies the quest for the perfect job.")
        st.markdown("---")
        # Mission statement
        st.write("Craftify is dedicated to empowering job seekers with the tools and insights necessary to thrive in today's competitive job market. Whether refining resumes or exploring new career avenues,Craftify stands as a trusted ally in the journey towards professional success and fulfillment.")
