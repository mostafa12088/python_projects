import imageio
import os

video_file = os.path.abspath(r"C:\\Users\\BME7ABT\\Desktop\\SampleVideo.mp4")

print(video_file)


def gifMaker(inputPath, targetFormate):
    outputPath = os.path.splitext(inputPath)[0] + targetFormate
    print(f"converting {inputPath} \n to {outputPath}")

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()["fps"]

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f"Frame {frames}")
    print("Gif Convertion Finished")
    writer.close()


gifMaker(video_file, ".gif")
