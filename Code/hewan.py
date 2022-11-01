class hewan:
  def __init__(self, nama, makan):
        self.nama = nama
        self.makan = makan

  def berjalan (self):
    print('hewan' , self.nama , 'dengan makan' , self.makan , 'hewan sedang berjalan')
    
  def tidur (self):
    print('hewan' , self.nama , 'dengan makan' , self.makan , 'hewan sedang tidur')

p5 = hewan('Kelinci' , "Wortel")
p6 = hewan('Harimau' , "Daging")
p7 = hewan('Kambing' , "Rumput")
    
p5 = hewan('Kelinci' , "Wortel")
p5.berjalan ()
p5.tidur ()

p6 = hewan('harimau' , "Daging")
p6.berjalan()
p6.tidur()

p7 = hewan('Kambing' , "Rumput")
p7.berjalan()
p7.tidur()
   