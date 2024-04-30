from faster_whisper import WhisperModel
import time

model_size = "small.en"



# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC
# VERY INPORTANT TOPIC

#================================================================
# to make it run on gpu made a copy of the file cublas64_11.dll at the path C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
# and renamed the copy to cublas64_12.dll
#================================================================


# Run on GPU with FP16
# model = WhisperModel(model_size, device="cpu", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8

t = time.time()
model = WhisperModel(model_size, device="cpu", compute_type="int8")
print("Time to load model: ", time.time() - t)

t = time.time()
segments, info = model.transcribe("Recording.m4a", beam_size=5)
print("Time to transcribe: ", time.time() - t)


print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

print(segments)
for i in segments:
    print(i)

