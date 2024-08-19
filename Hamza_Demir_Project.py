import random
import time

def rand_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def rand_choice1():
    return random.choice(['Taş', 'Kağıt', 'Makas'])

def comp_choice():
    return random.choice(['y','n'])

def comp_choice1():
    return random.choice(['e','h'])

print("Welcome to Rock/Paper/Scissors Game")


user_score = 0
computer_score = 0

while True:
    language = input("Please press '1' to play in Turkish.\nPress '2' to continue in English\nPress 'q' to exit\n")
    if language == '2':
        start = input("Press any key to start the game.\n(Press 'q' to exit)\n")

        if start.lower() == 'q':
            print("Exit is in progress")
            time.sleep(1.5)
            print("Have a good day")
            break

        print('Rule of the game: \nThe side that reaches 2 points wins the game.')
        print('Good luck.')

        while True:
            if user_score == 2:
                print("You won the game!")
                break
            elif computer_score == 2:
                print("Computer won the game!")
                break

            user = input("Your choice: ").lower()
            if user == 'q':
                print("Exiting the game.")
                break

            if user not in ['rock', 'paper', 'scissors']:
                print("Invalid input. Please select Rock, Paper or Scissors.")
                continue

            computer_choice = rand_choice()
            print("Choice of computer:", computer_choice)

            if user == computer_choice.lower():
                print("It's a tie!")
            elif (user == 'rock' and computer_choice == 'Scissors') or \
                 (user == 'paper' and computer_choice == 'Rock') or \
                 (user == 'scissors' and computer_choice == 'Paper'):
                print("You've won this round!")
                user_score += 1
            else:
                print("You lost this round.")
                computer_score += 1

            print(f"Score -> You: {user_score}, Computer: {computer_score}")

        while True:
            play_again = input("Do you want to play again? (Y/N): ").lower()

            if play_again == 'n':
                print("Thanks for playing! Goodbye.")
                break
            elif play_again == 'y':
                if user_score > computer_score:
                    print("This time I'll beat you")
                    time.sleep(1)
                    user_score = 0
                    computer_score = 0
                    break
                else:
                    print("I'm not sure about playing again because I won. Let me think about it")
                    time.sleep(3)
                    comp = comp_choice()
                    if comp != 'y':
                        print("I don't want to play again")
                        user_score = 0
                        computer_score = 0
                        break
                    else:
                        print("All right, let me beat you again.")
                        user_score = 0
                        computer_score = 0
                        break
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                continue
        if play_again == 'n':
            break

    #Türkçe Bölüm

    elif language == '1':
        start = input("Oyunu başlatmak için herhangi bir tuşa basın.\nÇıkmak için 'q' tuşuna basın\nNOT: Oyun Türkçe karakterlere duyarlıdır.\n")

        if start.lower() == 'q':
            print("Çıkış Yapılıyor...")
            time.sleep(1.5)
            print("İyi günler")
            break

        print('Oyunun kuralı: \n2 puana ulaşan taraf oyunu kazanır.')
        print("İyi Şanslar.")

        while True:
            if user_score == 2:
                print("Kazandın!")
                break
            elif computer_score == 2:
                print("Kaybettin!")
                break

            user = input("Seçimin: ").lower()
            if user == 'q':
                print("Çıkış Yapılıyor...")
                break

            if user not in ['taş', 'kağıt', 'makas']:
                print("Geçersiz giriş. Lütfen Taş, Kağıt veya Makas'ı seçin.")
                continue

            computer_choice = rand_choice1()
            print("Bilgisayar seçimi:", computer_choice)

            if user == computer_choice.lower():
                print("Berabere!")
            elif (user == 'taş' and computer_choice == 'Makas') or \
                    (user == 'kağıt' and computer_choice == 'Taş') or \
                    (user == 'makas' and computer_choice == 'Kağıt'):
                print("Bu Raundu Sen Kazandın!")
                user_score += 1
            else:
                print("Bu Raundu Kaybettin!")
                computer_score += 1

            print(f"Skor -> Sen: {user_score}, Bilgisayar: {computer_score}")

        while True:
            play_again = input("Tekrar oynamak ister misin? (E/H): ").lower()

            if play_again == 'h':
                print("Oynadığınız için teşekkürler! Güle güle.")
                break
            elif play_again == 'e':
                if user_score > computer_score:
                    print("Bu sefer seni yeneceğim.")
                    time.sleep(1)
                    user_score = 0
                    computer_score = 0
                    break
                else:
                    print("Kazandığım için tekrar oynamak konusunda emin değilim. Bir düşüneyim.")
                    time.sleep(3)
                    comp = comp_choice1()
                    if comp != 'e':
                        print("Tekrar oynamak istemiyorum.")
                        user_score = 0
                        computer_score = 0
                        break
                    else:
                        print("Pekala, seni tekrar yeneceğim.")
                        user_score = 0
                        computer_score = 0
                        break
            else:
                print("Geçersiz giriş. Lütfen Evet için 'E' veya Hayır için 'H' girin.")
                continue
        if play_again == 'h':
            break
    elif language == "q":
        print("İyi günler...")
        break

    else:
        print("Invalid login. Please try again")