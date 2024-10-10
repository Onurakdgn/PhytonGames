import random

try:
    def tas_kagit_makas():
        print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
        print("Kurallar:")
        print("1. Taş, makası kırar.")
        print("2. Makas, kağıdı keser.")
        print("3. Kağıt, taşı sarar.")
        print("İlk iki turu kazanan oyunu kazanır.")
        
        options = ["taş", "kağıt", "makas"]
        games_played = 0
        
        while True:
            player_wins = 0
            computer_wins = 0
            round_count = 0
            
            while player_wins < 2 and computer_wins < 2:
                round_count += 1
                print(f"\nTur {round_count}:")
                player_choice = input("Lütfen seçiminizi yapın (taş, kağıt, makas): ").lower()
                
                while player_choice not in options:
                    player_choice = input("Geçersiz seçim. Lütfen tekrar deneyin (taş, kağıt, makas): ").lower()
                
                computer_choice = random.choice(options)
                print(f"Bilgisayarın seçimi: {computer_choice}")
                
                if player_choice == computer_choice:
                    print("Bu tur berabere!")
                elif (player_choice == "taş" and computer_choice == "makas") or \
                     (player_choice == "makas" and computer_choice == "kağıt") or \
                     (player_choice == "kağıt" and computer_choice == "taş"):
                    print("Bu turu siz kazandınız!")
                    player_wins += 1
                else:
                    print("Bu turu bilgisayar kazandı!")
                    computer_wins += 1
            
            if player_wins == 2:
                print("\nTebrikler! Oyunu kazandınız!")
            else:
                print("\nBilgisayar oyunu kazandı! Tekrar deneyin.")
            
            games_played += 1
            play_again = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
            if play_again != "evet":
                break
        
        print(f"Oynanan oyun sayısı: {games_played}")
        print("Oyun bitti. İyi günler!")
    
    tas_kagit_makas()
except Exception as e:
    print(f"Hata: {e}")
