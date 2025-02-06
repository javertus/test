import time
import random

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def generate_order():
    pizzas = ["Margherita", "Pepperoni", "Vegetarian", "BBQ Chicken", "Meat Lovers"]
    return random.choice(pizzas)

def main():
    print_slow("📱 Saat 3:00 ve telefonuna gelen bir WhatsApp bildirimi seni uyandırıyor...")
    print_slow("📩 Müşteriden gelen mesaj: 'Acil! 8349+ pizza lazım!!!' 😱")
    print_slow("🏃 Pizzacı adam panikle dükkâna koşuyor!")
    
    score = 0
    start_time = time.time()
    time_limit = 60  # 60 saniye süren var!
    
    while time.time() - start_time < time_limit:
        order = generate_order()
        print_slow(f"📢 Yeni sipariş: {order} pizza! Çabuk yap! 🍕")
        
        response = input("Hangi pizzayı yapıyorsun? ").strip()
        
        if response.lower() == order.lower():
            print_slow("✅ Müşteri memnun! Bir sipariş daha tamamlandı! 🥳")
            score += 1
        else:
            print_slow("❌ Yanlış pizza! Müşteri sinirlendi! 😡")
        
    print_slow("⏳ Süre doldu! Bakalım kaç sipariş yetiştirdin...")
    print_slow(f"🎉 Toplam doğru sipariş: {score} pizza! 🍕")
    if score >= 10:
        print_slow("🔥 Sen gerçek bir pizza ustasısın!")
    else:
        print_slow("😢 İşler biraz sarpa sardı... Daha hızlı olmalısın!")

if __name__ == "__main__":
    main()
