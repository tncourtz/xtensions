#/bin/bash
ACCESS=`jq -r '.access_token' accesstoken.json `


# Get list of files
# curl -H "Authorization: Bearer ${ACCESS}" https://www.googleapis.com/drive/v3/files


curl  -H "Authorization: Bearer ${ACCESS}" --output bla.pdf https://www.googleapis.com/drive/v3/files/1jdTOCjmVNUPz7fq7ZdW89DdM-Iya0dvTDDwE6p_p6tw/export?mimeType=application/pdf