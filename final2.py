from telethon import TelegramClient, events
import asyncio
import time
# Replace with your actual API credentials
api_id = 22000513
api_hash = 'da739d9cdf83c12b1bf81521cf14b8ce'

# Replace with your actual phone number
phone_number = '+919381268838'

# Replace with your target usernames
#target_usernames = ['Buying_Selling_zone', 'THEHEISTNETWORKGROUP', 'otp_sellers_3', 'Escrowz_Network1', 'sellers_buyers_place', 'HDSMM_SELLERS', 'Scriptearninges', 'DEMON_SUPPORT', 'The_Official_Sellers', 'BuYeRssAnDsElLeRss', 'prosellertown_5', 'heistbuyandsell', 'Bhartiya_Group_3', 'Infinite_sellers', 'LUCIFERSELLING', 'CrAzckers', 'OPonlinepalengke', 'DARK_ESCROWS', 'Supersellers2', 'SELLERS_ARMY', 'heistbuyandselling4', 'FazeeMarket', 'Fantasy_Team_Somesh_Ram_Choudhar', 'SELLERSGANG', 'Indian_Seller_Group', 'hackbyzack', 'escrow1', 'Bhartiya_Group_7', 'SELLERSUNIVERSE', 'PREMIUM_SELLING_DEALZ', 'crack_account', 'rdp_buy_sell', 'THUNDERTEAM2', 'BHARTIYA_GROUP_6', 'IndianSellersCrew3', 'primesellingbuying', 'XENOMarket', 'BUYINGANDSELLING2', 'AwesomeBuyersSellers', 'RESELLERSHUB01', 'adsense_buy_and_sell', 'Bhartiya_Group_9', 'sellersandbuyers456', 'Bhartiya_Group_2', 'Bhartiya_Group_5', 'Sellinghub12288', 'SELLING_BUYING_GROUPS', 'prosellertown_2', 'BuySell98u', 'ONLY_ESCROW_SERVICEE', 'MGMART21334', 'IndianSellers3', 'SELLING_CITY', 'BHARTIYA_GROUP', 'NetflixDealZone', 'hidden_sellerss', 'prosellertown_1', 'indiansellerskingdom', 'THUNDERTEAM4', 'GM_MART', 'THUNDERTEAM3', 'wave_escrow', 'SINGHRESLLERSGROUP', 'Jodselling', 'Escrow_Adda', 'SELLERS_PLACE', 'SUMIT_RESELLERSCOMMUNITY', 'universal_selling_hub', 'escrowalwayss', 'blackmoneyhawalaa', 'SellingArmy', 'legit_selling_and_buying', 'piyushbuyandselling', 'TETHER_BULL', 'Indianotp_sellerr', 'onlinelocalshop', 'ResellersChatBGMI', 'Northern_Market_5', 'DEMON_PROMOTION', 'Sellers_Adda', 'coctrading', 'APSELLERS_14', 'UNIQUE_SELLERS', 'Selling_with_Escrowers', 'allaccontcheaprate', 'skullselling', 'sellerandbuyerescrow', 'SUPER_SELLERS_3', 'Dynamite_Selling_Group', 'thetrustedpremiumsellers', 'fuckingsellers', 'escrowworlds', 'BuyingSellingArena', 'SellingBuying_Network', 'SELLERS_Z0NE', 'escrowSELLERSxd', 'united_sellers11', 'Northern_Market_2', 'OnlinePremiumScoran', 'Escrowz_Network', 'Northern_Market', 'indianotp_sellerss', 'indian_otp_all_sellers', 'BuySellArena01', 'deal_via_escrow', 'Sellinghub12288_2', 'BeAsTSQuad_Selling', 'SellingbuyinClub', 'hellzkingdom', 'Sellingbuying_club', 'everythingsellandbuy', 'otp_sellers_indian', 'escrowonce_s', 'indian_otp_GROUP_SELLER_BUYER', 'IndianSellers4', 'only_escrow', 'SWARG_FREEFIRE_FF_BGMI_COC_PES', 'Excellent_sellers', 'MENTALSHOPPIE1', 'united_sellers6', 'CRIMINALSELLERS', 'NetflixOnAffordablePrice', 'Sellingmania', 'ErrorSelling', 'Resellers_Group', 'marketlegal', 'Northern_Market_3', 'indian_OtP_Seller2', 'Escrowz_Network2', 'dealershubs', 'Northern_Market_6', 'BuyAndSellAnythingGroup', 'premium_ac_selling', 'BuyingAndSellingDeals', 'MysticChats', 'otp_sellers_CyberAayan', 'Northern_Market_1', 'RAKURAICHATGROUP1', 'GLOBALXMARKET', 'Zatchxshopchat', 'gojo_igcc_talks']
target_usernames=['Buying_Selling_zone', 'THEHEISTNETWORKGROUP', 'otp_sellers_3', 'Escrowz_Network1', 'sellers_buyers_place', 'HDSMM_SELLERS', 'Scriptearninges', 'DEMON_SUPPORT', 'The_Official_Sellers', 'BuYeRssAnDsElLeRss', 'prosellertown_5', 'heistbuyandsell', 'Bhartiya_Group_3', 'Infinite_sellers', 'LUCIFERSELLING', 'CrAzckers', 'OPonlinepalengke', 'DARK_ESCROWS', 'Supersellers2', 'SELLERS_ARMY', 'heistbuyandselling4', 'FazeeMarket', 'Fantasy_Team_Somesh_Ram_Choudhar', 'SELLERSGANG', 'Indian_Seller_Group', 'hackbyzack', 'escrow1', 'Bhartiya_Group_7', 'SELLERSUNIVERSE', 'PREMIUM_SELLING_DEALZ', 'crack_account', 'rdp_buy_sell', 'THUNDERTEAM2', 'BHARTIYA_GROUP_6', 'IndianSellersCrew3', 'primesellingbuying', 'XENOMarket', 'BUYINGANDSELLING2', 'AwesomeBuyersSellers', 'RESELLERSHUB01', 'adsense_buy_and_sell', 'Bhartiya_Group_9', 'sellersandbuyers456', 'Bhartiya_Group_2', 'Bhartiya_Group_5', 'Sellinghub12288', 'SELLING_BUYING_GROUPS', 'prosellertown_2', 'BuySell98u', 'ONLY_ESCROW_SERVICEE', 'MGMART21334', 'IndianSellers3', 'SELLING_CITY', 'BHARTIYA_GROUP', 'NetflixDealZone', 'hidden_sellerss', 'prosellertown_1', 'indiansellerskingdom', 'THUNDERTEAM4', 'GM_MART', 'THUNDERTEAM3', 'wave_escrow', 'SINGHRESLLERSGROUP', 'Jodselling', 'Escrow_Adda', 'SELLERS_PLACE', 'SUMIT_RESELLERSCOMMUNITY', 'universal_selling_hub', 'escrowalwayss', 'blackmoneyhawalaa', 'SellingArmy', 'legit_selling_and_buying', 'piyushbuyandselling', 'TETHER_BULL', 'Indianotp_sellerr', 'onlinelocalshop', 'ResellersChatBGMI', 'Northern_Market_5', 'DEMON_PROMOTION', 'Sellers_Adda', 'coctrading', 'APSELLERS_14', 'UNIQUE_SELLERS', 'Selling_with_Escrowers', 'allaccontcheaprate', 'skullselling', 'sellerandbuyerescrow', 'SUPER_SELLERS_3', 'Dynamite_Selling_Group', 'thetrustedpremiumsellers', 'fuckingsellers', 'escrowworlds', 'BuyingSellingArena', 'SellingBuying_Network', 'SELLERS_Z0NE', 'escrowSELLERSxd', 'united_sellers11', 'Northern_Market_2', 'OnlinePremiumScoran', 'Escrowz_Network', 'Northern_Market', 'indianotp_sellerss', 'indian_otp_all_sellers', 'BuySellArena01', 'deal_via_escrow', 'Sellinghub12288_2', 'BeAsTSQuad_Selling', 'SellingbuyinClub', 'hellzkingdom', 'Sellingbuying_club', 'everythingsellandbuy', 'otp_sellers_indian', 'escrowonce_s', 'indian_otp_GROUP_SELLER_BUYER', 'IndianSellers4', 'only_escrow', 'SWARG_FREEFIRE_FF_BGMI_COC_PES', 'Excellent_sellers', 'MENTALSHOPPIE1', 'united_sellers6', 'CRIMINALSELLERS', 'NetflixOnAffordablePrice', 'Sellingmania', 'ErrorSelling', 'Resellers_Group', 'marketlegal', 'Northern_Market_3', 'indian_OtP_Seller2', 'Escrowz_Network2', 'dealershubs', 'Northern_Market_6', 'BuyAndSellAnythingGroup', 'premium_ac_selling', 'BuyingAndSellingDeals', 'MysticChats', 'otp_sellers_CyberAayan', 'Northern_Market_1', 'RAKURAICHATGROUP1', 'GLOBALXMARKET', 'Zatchxshopchat', 'gojo_igcc_talks', 'NORTHERN_MARKET', 'NORTHERN_MARKET_1', 'NORTHERN_MARKET_2', 'NORTHERN_MARKET_3', 'NORTHERN_MARKET_5', 'NORTHERN_MARKET_6', 'CCONRAD78', 'JERRYSELLING', 'SKULL_SUPPORT2', 'SKULL_SUPPORT3', 'SKULL_SUPPORT7', 'HIDDEN_SELLERSS', 'Bhartiya_Group', 'Bhartiya_Group_4', 'Bhartiya_Group_6', 'Bhartiya_Group_8', 'SELLINGHIDDEN', 'sellers_z0ne', 'LegitNetflixSelling', 'Accountdealers', 'OpFriendsZone', 'THUNDERTEAM5', 'nuclearselling', 'onlyfortrustedsellers', 'TEAM_DEVILS_KINGS', 'TSF_SELLERS', 'logomaker07bot', 'CRAZY_STORE01', 'mentalselling', 'IndianSellersCrew2', 'BEST_SELLINGS', 'buyingandsellingclub', 'IndianSellersCrew', 'otpbuyandselling', 'chattinglegends', 'buy_and_sell12', 'THUNDERTEAM9', 'ANKURSELLER1', 'SANiTY_GANG', 'SKULL_SUPPORT6', 'SKULL_SUPPORT5', 'SKULL_SUPPORT4', 'THE_OFFICIAL_SELLERS', 'SKULL_SUPPORT', 'HEISTBUYANDSELL', 'INFINITE_SELLERS', 'INDIAN_SELLER_GROUP', 'ESCROWCHATZ', 'SPACEX_SELLER01', 'INDIANSELLERS3', 'INDIANSELLERS4', 'SPACEX_SELLER02', 'HEISTBUYANDSELLING6', 'SPACEX_SELLER03', 'SUPERSELLERS2']
# Create a new TelegramClient instance
print(len(target_usernames))
client = TelegramClient('9381268838', api_id, api_hash)
group_username='@OttConnectShop'
async def main():
    await client.start(phone_number)

    # Fetch the group entity
    group = await client.get_entity(group_username)

    # Get the message history
    async for message in client.iter_messages(group):
        if(message.text!=None):
            for target_username in target_usernames:
                print(target_username + '    ' + str(message))
                await asyncio.sleep(0.8)
                t = time.localtime()
                current_time = time.strftime('%H:%M:%S', t)
                print(current_time)
                try:
                    await client.send_message(target_username, message)
                except Exception as err:
                    print(err)
            await asyncio.sleep(300)

for i in range(0,100):
    with client:
        client.loop.run_until_complete(main())
