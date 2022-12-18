import argparse
import os

import youtube_dl


def dl(url, out_path):

    os.makedirs('dl', exist_ok=True)

    fname = os.path.basename(out_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':  'dl/'+fname + '.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
             'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    return ydl.extract_info(url, download=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    dl(args.url, args.output)
