from flask import Flask,render_template,request,url_for
import pandas as pd
import numpy as np
import pickle
from output_module import output
from input_module import take_command,take_input


clf_mobile = pickle.load(open('model86%.pkl','rb'))
df_mobile = pickle.load(open('process.pkl', 'rb'))
clf_car = pickle.load(open('model3.pkl','rb'))
clf_bike = pickle.load(open('model90%.pkl','rb'))
clf_laptop = pickle.load(open('model46%.pkl','rb'))
df_laptop = pickle.load(open('processor_laptop.pkl','rb'))


def predict():
    selected=request.form.get('selected')
    print(selected)
    try:
        if selected == 'car':
            return render_template('index_car.html')
        elif selected == 'mobile':
            return render_template('index_mobile.html', df_mobile=df_mobile)
        elif selected == 'bike':
            return render_template('index_bike.html')
        elif selected == 'laptop':
            return render_template('index_laptop.html', df_laptop=df_laptop)
    except:

        return render_template('index.html')



def predict_car():

    try:
        output("List of company names (please select from the given list)")
        print("Maruti\nHyundai\nMahindra\nTata\nHonda\nToyota\nChevrolet\nRenault\nFord\nVolkswagen\nSkoda\nAudi\nMini\nBMW\nDatsun\nMitsubishi\nMercedes\n"
              "Nissan\nForce\nFiat\nHindustan\nJaguar\nLand\nVolvo\nJeep")
        output("what is the Company name of the car?")
        company = take_command()

        output("within 2000 to 2019")
        output("Which year you bought the car?")
        year = take_command()


        output("what is the fuel type of the car? petrol/diesel/lpg")
        fuel_type = take_command()
        output("The kilometer driven by the car(in kms)")
        kms_driven = take_command()
        company=company.lower()
        fuel_type.lower()
        company=company.capitalize()
        def change(text):
            if text == 'petrol':
                return 1
            elif text == 'diesel':
                return 2
            else:
                return 3
        fuel=change(fuel_type)

        d = {'company': company, 'year': year, 'kms_driven': kms_driven, 'fuel_type': fuel}
        data = pd.DataFrame(d, index=[1])

        new = pd.DataFrame(columns=['kms_driven', 'company_Audi', 'company_BMW', 'company_Chevrolet',
                                    'company_Datsun', 'company_Fiat', 'company_Force', 'company_Ford',
                                    'company_Hindustan', 'company_Honda', 'company_Hyundai',
                                    'company_Jaguar', 'company_Jeep', 'company_Land',
                                    'company_Mahindra', 'company_Maruti', 'company_Mercedes',
                                    'company_Mini', 'company_Mitsubishi', 'company_Nissan',
                                    'company_Renault', 'company_Skoda', 'company_Tata',
                                    'company_Toyota', 'company_Volkswagen', 'company_Volvo',
                                    'fuel_type_1', 'fuel_type_2', 'fuel_type_3', 'year_1995',
                                    'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
                                    'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009',
                                    'year_2010', 'year_2011', 'year_2012', 'year_2013', 'year_2014',
                                    'year_2015', 'year_2016', 'year_2017', 'year_2018', 'year_2019'])
        F = pd.get_dummies(data, columns=['company', 'fuel_type', 'year'])
        new[F.columns.values] = F[F.columns.values]
        new = new.replace(np.nan, 0)

        x = new.iloc[:, :].values
        pred=round(clf_car.predict(x)[0],2)

        output("You can sell your car at Rs. ")
        output(str(pred))

    except:

        output("Sorry, i am not sure what to suggest you based on the given informations!")


def predict_mobile():

    try:
        output("List of BRAND names (please select from the given list)")
        print("Apple\nSamsung\nXiaomi\nOppo\nOnePlus\nVivo\nNokia\nMotorola\nGoogle\nLG\nRealme\nHonor\nHTC\nMicromax\nGionee\nGeneral\nHuaweiInFocus\nPanasonic\nAsus")
        output("what is the brand of the mobile phone?")
        brand=take_command()

        output("How much is the ram of the mobile phone?")
        output("options - 1 GB/2 GB/3 GB/4 GB/6 GB/8 GB/12 GB")
        ram=take_command()
        output("what is the internal storage capacity of the mobile phone?")
        output("options - 1 GB/8 GB/16 GB/32 GB/64 GB/128 GB/512 GB")
        rom=take_command()
        output("what is the screen size of the mobile phone?")
        screen=take_command()
        output("what is the range of primary camera of the mobile phone?")
        Primary_cam=take_command()
        output("what is the range of front camera of the mobile phone?")
        front_cam=take_command()
        #output("what is the processor name of the mobile phone?")
        #processor_cost=take_command()
        screen=screen.lower().strip('inch')
        Primary_cam=Primary_cam.lower().strip('megapixel')
        front_cam=front_cam.lower().strip('megapixel')
        Primary_cam = Primary_cam.lower().strip('mp')
        front_cam = front_cam.lower().strip('mp')


        new = pd.DataFrame(columns=['screen_size', 'Primary_cam', 'front_cam', 'brand_Apple',
                                    'brand_Asus', 'brand_General', 'brand_Gionee', 'brand_Google',
                                    'brand_HTC', 'brand_Honor', 'brand_Huawei', 'brand_InFocus',
                                    'brand_LG', 'brand_Micromax', 'brand_Motorola', 'brand_Nokia',
                                    'brand_OnePlus', 'brand_Oppo', 'brand_Panasonic', 'brand_Realme',
                                    'brand_Samsung', 'brand_Vivo', 'brand_Xiaomi', 'ram_1', 'ram_2',
                                    'ram_3', 'ram_4', 'ram_6', 'ram_8', 'ram_12', 'rom_1', 'rom_8',
                                    'rom_16', 'rom_32', 'rom_64', 'rom_128', 'rom_256', 'rom_512'])
        d = {'brand': brand, 'screen_size': screen, 'Primary_cam': Primary_cam, 'front_cam': front_cam,
             'ram': ram, 'rom': rom}
        data = pd.DataFrame(d, index=[1, 2])
        F = pd.get_dummies(data, columns=['brand', 'ram', 'rom'])
        new[F.columns.values] = F[F.columns.values]
        new = new.replace(np.nan, 0)
        x = new.iloc[:, :].values
        p1=round(clf_mobile.predict(x)[0],2)
        p2=round(clf_mobile.predict(x)[0],2)/2.5
        pred=round(p1-p2)#+int(processor_cost)

        output("You can sell your mobile phone at Rs. ")
        output(str(pred))

    except:

        output("Sorry, i am not sure what to suggest you based on the given informations!")


def predict_bike():
    try:
        output("Select from the list below")
        print("Bajaj\nHonda\nHero\nRoyal\nYamaha\nTVS\nSuzuki\nKTM\nHarley\nLML\nAprilia\nMahindra\nKawasaki\nBenelli\nTriumph\nHyosung\nDucati\nJawa\nLambretta\nBMW\nKinetic\nYezdi")
        output("What is the company of your bike?")
        brand=take_command()
        output("within 1996 to 2019")
        output("Which year you bought the bike?")
        year=take_command()
        output("The kilometer driven by the bike(in kms)")
        distance=take_command()
        distance=distance.strip('kms')
        year=" "+year
        new=pd.DataFrame(columns=['distance', 'brand_Aprilia', 'brand_BMW', 'brand_Bajaj',
       'brand_Benelli', 'brand_Ducati', 'brand_Harley', 'brand_Hero',
       'brand_Honda', 'brand_Hyosung', 'brand_Jawa', 'brand_KTM',
       'brand_Kawasaki', 'brand_Kinetic', 'brand_LML', 'brand_Lambretta',
       'brand_Mahindra', 'brand_Royal', 'brand_Suzuki', 'brand_TVS',
       'brand_Triumph', 'brand_UM', 'brand_YO', 'brand_Yamaha',
       'brand_Yezdi', 'year_ 1996', 'year_ 1997', 'year_ 1998',
       'year_ 1999', 'year_ 2000', 'year_ 2001', 'year_ 2002',
       'year_ 2003', 'year_ 2004', 'year_ 2005', 'year_ 2006',
       'year_ 2007', 'year_ 2008', 'year_ 2009', 'year_ 2010',
       'year_ 2011', 'year_ 2012', 'year_ 2013', 'year_ 2014',
       'year_ 2015', 'year_ 2016', 'year_ 2017', 'year_ 2018',
       'year_ 2019', 'year_ Before 1995'])

        d = {'brand': brand, 'year': year, 'distance': distance}
        data = pd.DataFrame(d, index=[1])
        F = pd.get_dummies(data, columns=['brand', 'year'])
        new[F.columns.values] = F[F.columns.values]
        new = new.replace(np.nan, 0)
        x = new.iloc[:, :].values
        pred = round(clf_bike.predict(x)[0], 2)

        output("You can sell your Bike at Rs. ")
        output(str(pred))

    except:

        output("Sorry, i am not sure what to suggest you based on the given informations!")


def predict_laptop():
    try:
        output("What is the product type? Laptop or Desktop" )
        product_type=take_command()
        output("Please Select from the list below ")
        print("Dell\nHP ( Hewlett-Packard)\nLenovo\nApple\nAcer\nAsus\nSony\nToshiba\nOthers\nSamsung\nCompaq\nHCL\nMSI\nWipro\nFujitsu-Siemens\nLG"
              "Microsoft\nWD Western Digital\nMicromax Laptab\nFujitsu\nAlldocube\nE Machines\nSolt\nZED LIFE\n")
        output("what is the brand of the laptop?")
        brand=take_command()
        output("What is the ram capacity of the laptop")
        output("options - 1 GB/2 GB/3 GB/4 GB/6 GB/8 GB/12 GB")
        ram=take_command()
        output("How is the condition of the laptop? Gently Used or Almost Like New or Brand New or Heavily Used or Used or Unboxed or New")
        condition=take_command()
        output("What is the screen size of the laptop (in inches)")
        screen=take_command()
        #processor_cost=take_command()
        ram=ram.strip(' GB')
        screen=screen.strip('inch')

        new = pd.DataFrame(columns=['Ram', 'screen', 'brand_Acer', 'brand_Alldocube', 'brand_Apple',
                                    'brand_Asus', 'brand_Compaq', 'brand_Dell', 'brand_E Machines',
                                    'brand_Fujitsu', 'brand_Fujitsu-Siemens', 'brand_Gateway',
                                    'brand_HCL', 'brand_HP ( Hewlett-Packard)',
                                    'brand_High Quality Assembled Desktop with Laptop Table',
                                    'brand_LG', 'brand_Lenovo', 'brand_MSI', 'brand_Micromax Laptab',
                                    'brand_Microsoft', 'brand_Others', 'brand_RDP THINBOOK 1310',
                                    'brand_Reach Rcn025', 'brand_Samsung', 'brand_Solt', 'brand_Sony',
                                    'brand_Toshiba', 'brand_Tripod brand new',
                                    'brand_WD Western Digital', 'brand_Wipro', 'brand_ZED LIFE',
                                    'product_type_Desktop', 'product_type_Laptop',
                                    'condition_Almost Like New', 'condition_Brand New',
                                    'condition_Gently Used', 'condition_Heavily Used', 'condition_New',
                                    'condition_Unboxed', 'condition_Used'])
        d = {'brand': brand, 'screen': screen, 'Ram': ram, 'condition': condition, 'product_type': product_type}
        data = pd.DataFrame(d, index=[1])
        F = pd.get_dummies(data, columns=['brand', 'product_type', 'condition'])
        new[F.columns.values] = F[F.columns.values]
        new = new.replace(np.nan, 0)
        x = new.iloc[:, :].values
        pred = round(clf_laptop.predict(x)[0], 2)#+int(processor_cost)

        output(f"You can sell your {product_type} at Rs. ")
        output(str(pred))

    except:

        output("Sorry, i am not sure what to suggest you based on the given informations!")


