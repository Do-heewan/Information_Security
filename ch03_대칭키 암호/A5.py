# 3-1 A5/1 알고리즘

class SimpleLSFR:
    def __init__(self, size, taps, clock_bit):
        self.size = size
        self.taps = taps # 피드백 비트
        self.clock_bit = clock_bit # 클락 비트

        self.state = [0] * size # 현재 상태
    
    def feedback(self):
        fb = 0
        for ix in self.taps:
            fb ^= self.state[ix]
        
        return fb
    
    def clock(self, bit=0):
        fb = self.feedback() ^ bit
        out = self.state[-1]

        self.state = [fb] + self.state[:-1]

        return out

    def get_clock_bit(self):
        return self.state[self.clock_bit]
    
    def majority(a, b, c):
        return (a & b) | (a & c) | (b & c)


class SimpleA5:
    def __init__(self, key, frame):
        self.key = key
        self.frame = frame

        self.X = SimpleLSFR(5, [2, 4], 2)
        self.Y = SimpleLSFR(6, [1, 5], 3)
        self.Z = SimpleLSFR(7, [1, 5, 6], 4)

        self.init_registers(key, frame)

    def init_registers(self, key, frame):

        # Key 로딩
        for i in range(16):
            bit = (key >> i) & 1
            self.X.clock(bit)
            self.Y.clock(bit)
            self.Z.clock(bit)

        # frame 로딩
        for i in range(8):
            bit = (frame >> i) & 1
            self.X.clock(bit)
            self.Y.clock(bit)
            self.Z.clock(bit)

        # 위밍업 10회
        for _ in range(10):
            maj = SimpleLSFR.majority(self.X.get_clock_bit(), self.Y.get_clock_bit(), self.Z.get_clock_bit())

            if (self.X.get_clock_bit() == maj):
                self.X.clock()
            if (self.Y.get_clock_bit() == maj):
                self.Y.clock()
            if (self.Z.get_clock_bit() == maj):
                self.Z.clock()
    
    def get_keystream_bit(self):
        maj = SimpleLSFR.majority(self.X.get_clock_bit(), self.Y.get_clock_bit(), self.Z.get_clock_bit())

        if (self.X.get_clock_bit() == maj):
            self.X.clock()
        if (self.Y.get_clock_bit() == maj):
            self.Y.clock()
        if (self.Z.get_clock_bit() == maj):
            self.Z.clock()

        return self.X.state[-1] ^ self.Y.state[-1] ^ self.Z.state[-1]

    def get_keystream(self, nbits):
        stream = 0
        for _ in range(nbits):
            stream = (stream << 1) | self.get_keystream_bit()

        return stream

#===== 테스트 ======
a5 = SimpleA5(0xBEEF, 0x3A)
# print("10진수 :", a5.get_keystream)
print("키스트림 :", bin(a5.get_keystream(8)))