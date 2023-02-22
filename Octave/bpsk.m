%bpsk simulation and theoretical proof
R = 1; %for uncoded bpsk
EbNodb = 10.5;
EbNo = 10^(EbNodb/10);
sigma = sqrt(1/(2*R*EbNo));

%simulation approach
N = 1000;
blocks = 100;
errors = 0;
for i = 1 : blocks
  msg = randi([0 1],1,N);
  symb = 1-2*msg;%bit to symbols conversion
  n = symb + sigma * randn(1,N);%received bits with noise
  decision_dev = (n<0);% decision device
  errors = errors+ sum(msg ~=decision_dev);
end
ber_sim = errors/N;%finding bit error rate

% theoretical approach
ber_theo = 0.5*erfc(sqrt(R*EbNo));
disp([EbNodb ber_theo ber_sim errors N*blocks]);
