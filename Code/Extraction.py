import os, re
def cut(video_file_path, start_time, end_time):
    """ cuts the video using ffmpeg using the start and end time and the video
    Keyword arguments:
    video_file_path -- full path to the video
    start_time -- string of time in HH:MM:SS:ff format
    end_time -- string of time in HH:MM:SS:ff format
    """
    output_file_path = re.search("^[\/].+\/", video_file_path)
    output_file_path_raw = output_file_path.group(0)
    delsplit = re.search("\/(?:.(?!\/))+$", video_file_path)
    filename = re.sub("^[\/]", "", delsplit.group(0))
    filename_raw = re.sub(".{4}$", "", filename)
    file_extension = re.search(".{3}$", filename)
    file_extension_raw = file_extension.group(0)

    os.environ['inputFile'] = video_file_path
    os.environ['outputPath'] = output_file_path_raw
    os.environ['startTime'] = start_time
    os.environ['endTime'] = end_time
    os.environ['fileName'] = filename_raw
    os.environ['fileExtension'] = file_extension_raw

    !ffmpeg -hide_ban
    ner -i "$inputFile" -ss "$startTime" -to "$endTime" -c copy "$outputPath"/"$fileName"-TRIM."$fileExtension"