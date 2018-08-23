gspeech
=======

ROS package for speech recognition based on Google Cloud Speech API



NOTE: This package needs an API key to use the Speech API. Each request is accepted if the audio duration is less than 15 seconds.

For key generation follow the following steps:
1. Create a project in the [Google Cloud Platform Console](https://console.cloud.google.com/)
2. Make note of the project ID 
3. Set up an [API key](https://support.google.com/googleapi/answer/6158862?hl=en)
4. Enable billing for the project (Google offers a free 1 year trial)
5. Enable the [Cloud Speech API](https://support.google.com/cloud/answer/6158841?hl=en)
6. Install the [Cloud SDK](https://cloud.google.com/sdk/)
7. Authenticate to the [Cloud API](https://cloud.google.com/docs/authentication/getting-started) 
8. Add API key variable to environment *export GOOGLE_API_KEY=*  

Usage
-----
`roslaunch gspeech gspeech.launch`
