import cv2

def concatenate_videos(video_path1, video_path2, output_path, scale_factor=0.5, fps_output=30):
    # 打开两个视频文件
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    # 获取视频的帧率（fps）和帧大小
    fps1 = cap1.get(cv2.CAP_PROP_FPS)
    fps2 = cap2.get(cv2.CAP_PROP_FPS)

    if fps1 != fps2:
        print("Warning: The two videos have different frame rates!")

    # 获取视频的宽度和高度
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 确保两个视频的高度相同，若不同，则将其中一个视频调整为相同高度
    if height1 != height2:
        new_height = min(height1, height2)
        cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, new_height)
        cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, new_height)

    # 输出视频的宽度是两个视频的宽度之和
    output_width = width1 + width2
    output_height = max(height1, height2)

    # 根据 scale_factor 缩放分辨率
    output_width = int(output_width * scale_factor)
    output_height = int(output_height * scale_factor)

    # 创建视频写入对象，使用H264编码
    fourcc = cv2.VideoWriter_fourcc(*'H264')  # H264编码
    out = cv2.VideoWriter(output_path, fourcc, fps_output, (output_width, output_height))

    # 遍历两个视频的帧，进行拼接
    while cap1.isOpened() and cap2.isOpened():
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break  # 如果任意一个视频读取完毕，则退出

        # 缩放视频帧
        frame1_resized = cv2.resize(frame1, (int(width1 * scale_factor), int(height1 * scale_factor)))
        frame2_resized = cv2.resize(frame2, (int(width2 * scale_factor), int(height2 * scale_factor)))

        # 将两个帧横向拼接
        combined_frame = cv2.hconcat([frame1_resized, frame2_resized])

        # 写入拼接后的帧
        out.write(combined_frame)

    # 释放资源
    cap1.release()
    cap2.release()
    out.release()

    print("视频拼接完成，输出文件为:", output_path)

    
# 调用函数，传入视频文件路径和输出路径
video1 = 'D:\\Dev_code\\2DGS-Room\\static\\videos\\scene0050_00_2dgs.mp4'
video2 = 'D:\\Dev_code\\2DGS-Room\\static\\videos\\scene0050_00_ours.mp4'
output = 'D:\\Dev_code\\2DGS-Room\\static\\videos\\scene0050_00.mp4'
concatenate_videos(video1, video2, output)
