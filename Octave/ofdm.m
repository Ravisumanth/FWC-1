bps = 6; % bits per symbol
M = 2^bps;%type of QAM
nfft = 256; %no. of fft bins or length of symbol
ncp = 16; %length of cp
msg = randi([0 M-1],nfft,1);
msg = reshape(msg,[1,nfft]);
%display(msg);
SNR = 40; %in dB
mod_msg = qammod(msg,M);%16 QAM is achieved
%display(mod_msg);
tran_msg = ifft(mod_msg,nfft);%applying inverse fft to the msg bits (orthogonality is achieved here)
%display(tran_msg);

%create channel impulse response and covolute with msg signal
h = randi([0 5], 3
, 1);%channel impulse response
h = reshape(h,[1,3]);
%display(h);
%adding CP to symbols
cp = tran_msg(nfft-ncp+1:nfft);
%display(cp);

msg_cp = [cp tran_msg];
%display(msg_cp);

noisy_msg_cp = awgn(msg_cp,SNR);
%display(noisy_msg_cp);

conv_msg_cp = cconv(noisy_msg_cp,h,length(msg_cp)+length(h)-1);%convolution is done.
%display(conv_msg_cp);

conv_msg = conv_msg_cp(length(conv_msg_cp)-ncp:end);
%display(conv_msg);

rec_msg = fft(conv_msg,nfft);
%display(rec_msg);

demod_msg = qamdemod(rec_msg,M);
%display(demod_msg);
ans = max(msg - demod_msg);
if ans < 1e-8
  display("Match");
 else
  display("Mismatch");
 end



