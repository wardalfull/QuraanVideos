import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Wedad Saleh Studio!</title>
    <meta name="Author" content="Wedad Saleh">
    
        <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #311b31;
            color: #CCC;
        }
        #video .modal-dialog {
            margin-top: 200px;
            width: 840px;
            height: 500px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #video-video {
            width: 100%;
            height: 100%;
        }
        .video-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .video-tile:hover {
            background-color: #ff9999;
            cursor: pointer;
        }
        .video-tile img {
            box-shadow: 7px 7px 12px #222;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: red;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#video-video-container").empty();
        });
        // Start playing the video whenever the modal is opened
        $(document).on('click', '.video-tile', function (event) {
            var youTubeId = $(this).attr('data-video-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + youTubeId + '?autoplay=1&html5=1';
            $("#video-video-container").empty().append($("<iframe></iframe>", {
              'id': 'video-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the videos when the page loads
        $(document).ready(function () {
          $('.video-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Video Video Modal -->
    <div class="modal" id="video">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="video-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Wedad Saleh Studio</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {video_tiles}
    </div>
  </body>
</html>
'''

# A single video entry html template
video_tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" data-video-youtube-id="{video_youtube_id}" data-toggle="modal" data-target="#video">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{video_title}</h2>
    <p>{video_storyline}</p>
    <p>Release date: {video_release_date}</p>
</div>
'''

def create_video_tiles_content(videos):
    # The HTML content for this section of the page
    content = ''
    for video in videos:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.video_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         video.video_youtube_url)
        video_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the video with its content filled in
        content += video_tile_content.format(
            video_title=video.title,
            video_storyline=video.storyline,
            poster_image_url=video.poster_image_url,
            video_youtube_id=video_youtube_id,
            video_release_date=video.release_date
        )
    return content

def open_videos_page(videos):
    # Create or overwrite the output file
    output_file = open('Wedad Saleh.html', 'w')

    # Replace the placeholder for the video tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(video_tiles=create_video_tiles_content(videos))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
