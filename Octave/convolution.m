x = [1 2 -3 4 0 5 6];
y = [2 3 -4];

lin_conv = conv(x,y);%linear convolution of 2 signals. To use dft for linear convolution, we have to pad the signals such that their length>=x1+x2-1
display(lin_conv);
%for circular convolution, we need to have both signals of equal length. we need to apply fourier transform to signals and multiply them. finally, we have to inverse the fft on the product.
x_pad = [x zeros(1,length(y)-1)];
y_pad = [y zeros(1,length(x)-1)];
cir_conv = ifft(fft(x_pad).*fft(y_pad));%circular convolution of signals after padding
display(cir_conv);
display(length(cir_conv));
theo_cconv = cconv(x_pad,y_pad,9);
display(theo_cconv);
display(length(theo_cconv));
