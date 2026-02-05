clear; clc;




%% Load baseline data
baseline = readtable("baseline.csv");

t = baseline.t_s;        % time vector
x = baseline.flame_signal;     % baseline signal (ADC values)

fs = 1;                  % sampling frequency (Hz)

%% FIR Low-pass filter design
N  = 10;                 % filter order
fc = 0.15;                % cutoff frequency (Hz)

Wn = fc / (fs/2);        

b = fir1(N, Wn, 'low', hamming(N+1));

%% Apply filter
x_filt = filtfilt(b, 1, x);

%% Plot results
figure
subplot(2,1,1)
plot(t, x)
title('baseline Signal (Before Filtering)')
xlabel('Time (s)')
ylabel('Amplitude')

subplot(2,1,2)
plot(t, x_filt)
title('baseline Signal (After FIR Low-pass Filtering)')
xlabel('Time (s)')
ylabel('Amplitude')