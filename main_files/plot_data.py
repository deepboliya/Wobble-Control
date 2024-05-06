import numpy as np
import matplotlib.pyplot as plt

# Specify the absolute path of the file
file_path_1 = 'main_files/bot_ypr_pqr_data_actuated_pendulum2.txt'  # Update this to the correct file path
file_path_2 = 'main_files/bot_ypr_pqr_data_collect1.txt'  # Update this to the correct file path

# Read the data from the file
data_1 = np.loadtxt(file_path_1, skiprows=1)
data_2 = np.loadtxt(file_path_2, skiprows=1)


# Assuming the columns are Timestamp, Yaw, Pitch, Roll
timestamps_1 = data_1[:, 0]
yaw_1 = data_1[:, 1]
pitch_1 = data_1[:, 2]
roll_1 = data_1[:, 3]
p_1 = data_1[:,4]
q_1 = data_1[:,5]
r_1 = data_1[:,6]

timestamps_2 = data_2[:, 0]
yaw_2 = data_2[:, 1]
pitch_2 = data_2[:, 2]
roll_2 = data_2[:, 3]
p_2 = data_2[:,4]
q_2 = data_2[:,5]
r_2 = data_2[:,6]

# Plotting the data
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(timestamps_1, r_1, label='Roll Rate with Stabilization')
plt.plot(timestamps_2, r_2, label='Roll Rate without Stabilization')
plt.title('Yaw over Time')
plt.ylabel('Degrees')
plt.legend()
# plt.subplot(2, 1, 2)
# plt.plot(timestamps_1, pitch_1, label='Pitch_1')
# plt.plot(timestamps_2, pitch_2, label='Pitch_2')

# plt.title('Pitch over Time')
# plt.ylabel('Degrees')

plt.subplot(2, 1, 2)
plt.plot(timestamps_1, roll_1, label='Roll Stabilized')
plt.plot(timestamps_2, roll_2, label='Roll Not stabilized')

plt.title('Roll over Time')
plt.ylabel('Degrees')

plt.xlabel('Timestamp')
plt.tight_layout()
plt.legend()
plt.show()
