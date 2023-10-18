MIN_READING = 0
MAX_READING = 999999999

RESIDENTIAL_BASIC = 5.00
RESIDENTIAL_PER_GALLON = 0.0005

COMMERCIAL_BASIC = 1000.00
COMMERCIAL_CUTOFF = 4000000
COMMERCIAL_PER_GALLON = 0.00025

INDUSTRIAL_BASIC_1 = 1000.00
INDUSTRIAL_CUTOFF_1 = 4000000
INDUSTRIAL_BASIC_2 = 2000.00
INDUSTRIAL_CUTOFF_2 = 10000000
INDUSTRIAL_PER_GALLON = 0.00025

customer_code = input('Enter customer code (R, C, or I):')

if customer_code not in ['R','C','I']:
    print('Invalid input (customer code)')

else:
    start_reading = int(input('Enter beginning reading (between 0 and 999999999):'))
    end_reading = int(input('Enter ending reading (between 0 and 999999999):'))

    if not(MIN_READING <= start_reading <= MAX_READING) or  not(MIN_READING <= end_reading <= MAX_READING):
       print('Invalid input (beginning or ending reading value is out of the range)')

    else:
        if end_reading < start_reading:
            used_gallons = (MAX_READING + 1 - start_reading + end_reading) / 10
        else:
            used_gallons = (end_reading / 10) - (start_reading / 10)

        if customer_code == 'R':
           to_bill = RESIDENTIAL_BASIC + RESIDENTIAL_PER_GALLON * used_gallons

        elif customer_code == 'C':
           if used_gallons <= COMMERCIAL_CUTOFF:
              to_bill = COMMERCIAL_BASIC
           else:
               to_bill = COMMERCIAL_BASIC + COMMERCIAL_PER_GALLON * (used_gallons - COMMERCIAL_CUTOFF)

        else:
            if used_gallons <= INDUSTRIAL_CUTOFF_1:
               to_bill = INDUSTRIAL_BASIC_1

            elif used_gallons <= INDUSTRIAL_CUTOFF_2:
               to_bill = INDUSTRIAL_BASIC_2

            else:
                to_bill = INDUSTRIAL_BASIC_2 + INDUSTRIAL_PER_GALLON * (used_gallons - INDUSTRIAL_CUTOFF_2)

        print(f'Customer code: {customer_code}')
        print(f'Beginning reading value in gallons and tenths of gallon {start_reading / 10.0:.1f}')
        print(f'Ending reading value in gallons and tenths of gallon {end_reading / 10.0:.1f}')
        print(f'Gallons of water used: {used_gallons:.1f}')
        print(f'Amount billed: ${to_bill:.2f}')
