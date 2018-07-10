import video_page
import webbrowser
import media

surah_AlHaqqah = media.Myvideo("Surah Al-Haqqah", "The Surah takes its name from the word al-Haaqqah with which it opens. This Surah has 52 verses ",
                        "http://www5.0zz0.com/2018/06/30/15/573970929.jpg",
                        "https://www.youtube.com/watch?v=TBgc1Fx-rkU", "May 3, 2008")

surah_AlSajdah = media.Myvideo("Surah Al-Sajdah", "It takes its name cause of the believers who worship Allah and praise Him when they hear Qur'an",
                        "http://www10.0zz0.com/2018/06/30/16/246142428.jpg",
                        "https://www.youtube.com/watch?v=wWOyksrS3Ks","May 9, 2012")

Surah_AlQiyamah = media.Myvideo("Surah Al-Qiyamah",
                          "Surah (Chapter) Number: 75"
                          "Number of Verses: 40 English Meaning: The Resurrection",
                          "http://www2.0zz0.com/2018/06/30/16/564226457.jpg",
                          "https://www.youtube.com/watch?v=OipsnyvU2K0","Nov 18, 2012")

Surah_AlMulk = media.Myvideo("Surah Al-Mulk",
                          "The Surah takes its name al-Mulk from the very first sentence."
                          "This Surah has 30 verses and resides between pages 562 to 564 in the Quran",
                          "http://www10.0zz0.com/2018/06/30/17/683793881.jpg",
                          "https://www.youtube.com/watch?v=v88nypUNhBo","Jun 5, 2013")

Surah_AdDukhan = media.Myvideo("Surah Ad-Dukhan",
                         "The Surah takes its name from the word dukhan which occurs in verse 10. This Surah has 59 verses and resides between pages 496 to 498 in the Quran",
                         "http://www10.0zz0.com/2018/06/30/17/396504827.jpg", 
                         "https://www.youtube.com/watch?v=RlK4RrkCfdg","Dec 2, 2016")

Surah_alTur = media.Myvideo("Surah al-Tur",
                           "The 52nd sura of the Qur'an with 49 ayat. The surah that opens with the oath of the Divine One swearing by the Mount of Sinai",
                           "http://www14.0zz0.com/2018/06/30/18/582312842.jpg",
                           "https://www.youtube.com/watch?v=QjY98nWaP6M","Jan 17, 2011")


    # Store the objects in a list.
videos = [surah_AlHaqqah, surah_AlSajdah, Surah_AlQiyamah, Surah_AlMulk, Surah_AdDukhan, Surah_alTur]
video_page.open_videos_page(videos)
