/*
 * PWM.c.c
 *
d * Created: 2/2/2019 3:34:55 PM
 * Author : Meet
 */

#include<avr/io.h>
#include<util/delay.h>
#include<stdlib.h>
#include<string.h>
// define some macros
#define BAUDrate 9600
#define FOSC 8000000UL                                 // define baud
#define ubrr 51
int q,i,j;
void uart_init (int baud)
{   // to establish uart 0
	UBRR0H = (unsigned char)(baud>>8);                      // shift the register right by 8 bits
	UBRR0L =(unsigned char) baud;                           // set baud rate
	UCSR0B |= (1<<RXEN0)|(1<<TXEN0);                     // 4 rxen and 3 txen
	// enable receiver and transmitter
	UCSR0C=0b10000110;         //stop bit 1 ,parity=None,bits=8
}
void USART_Transmit( unsigned char data )

{

	/* Wait for empty transmit buffer */

	while ( !( UCSR0A & (1<<UDRE0)) );
		UDR0 = data;
	/* Put data into buffer, sends the data */
}
unsigned char USART_Receive( void )

{

	/* Wait for data to be received */

	while ( !(UCSR0A & (1<<RXC0)) );

	/* Get and return received data from buffer */

	return UDR0;
}
void setval1C( int va)             
{	va=va*100;
	OCR1CH=(va>>8);
	OCR1CL=va;
}
void setval1B( int va)
{	va=va*100;
	OCR1BH=(va>>8);
	OCR1BL=va;
}
void setval1A( int va)
{	va=va*100;
	OCR1AH=(va>>8);
	OCR1AL=va;
}
int main()
{
	char a;
	DDRB=0xFF;
	PORTB|=(1<<PINB5)|(1<<PINB6)|(1<<PINB7); //enabling pins OC1A,OC1B,OC1C
	TCCR1A|=(1<<COM1A1)|(1<<WGM11)|(1<<COM1B1)|(1<<COM1C1); //COMC1  FOR FAST PWM
	TCCR1B|=(1<<WGM12)|(1<<WGM13)|(1<<CS10);	// WGMx11-12-13 ARE FOR
	ICR1=0x2710;	//SETTING UP TOP AT 10000
	uart_init(51);
	char data;
	int j;
	//data=USART_Receive();
	//USART_Transmit(data);
	setval1C(0);
	setval1B(0);
	setval1A(0);
	while(1)
	{    
		data=USART_Receive();
		_delay_ms(100);
		USART_Transmit(data);
		_delay_ms(100);
		switch(data)
		{
			case 'b':	//all on
			setval1A(100);
			setval1B(100);
			setval1C(100);
				break;
				
			case 'a':	//all off
			setval1A(0);
			setval1B(0);
			setval1C(0);
			break;
				
			case 'c':	//1 on
			setval1A(100);
			setval1B(0);
			setval1C(0);
			break;
				
			case 'd':	//2 on
			setval1A(0);
			setval1B(100);
			setval1C(0);

				break;

			case 'e':	//3 on
			setval1A(0);
			setval1B(0);
			setval1C(100);
			break;

			case 'f':	//1 and 2 on
			setval1A(100);
			setval1B(100);
			setval1C(0);
			break;

			case 'g':	//1 and 3 on
			setval1A(100);
			setval1B(0);
			setval1C(100);
			break;
			
			case 'h':	//2 and 3 on
			setval1A(0);
			setval1B(100);
			setval1C(100);
			break;

			case 'i':  //1 with 25%
			setval1A(25);
			setval1B(0);
			setval1C(0);
			break;
			
			case 'j':  //1 with 75%
			setval1A(75);
			setval1B(0);
			setval1C(0);
			break;
			
			case 'k':  //2 with 25%
			setval1A(0);
			setval1B(25);
			setval1C(0);
			break;

			case 'l':  //2 with 75%
			setval1A(0);
			setval1B(75);
			setval1C(0);
			break;
			
			case 'm':  //3 with 25%
			setval1A(0);
			setval1B(0);
			setval1C(25);
			break;

			case 'n':  //3 with 75%
			setval1A(0);
			setval1B(0);
			setval1C(75);
			break;

			case 'o':  //1 off
			setval1A(0);
			break;

			case 'p': 
			 //dim to high
			 while(1) 
			{	j=1;
				for(i=5;i<=100;i+=5)
				{	
				if(j==1)
				setval1A(i);
				if(j==2)
				setval1B(i);
				if(j==3)
				setval1C(i);
				if(j==6)
				setval1A(i);
				if(j==5)
				setval1B(i);
				if(j==4)
				setval1C(i);
				if(j==6)
				  j=1;
				  
				j++;
				_delay_ms(500);
		}if(UDR0=='x')
		{
			setval1A(0);
			setval1B(0);
			setval1C(0);
			break;
		}
			}
			break;

			case 'q':  //3 off
			setval1C(0);
			break;
			
			case 'r':  //2 off
			setval1B(0);
			break;
			
			case 's': //dancing
			while(1)
			{
				setval1A(100);
				setval1B(0);
				setval1C(0);
				_delay_ms(1000);
				setval1A(0);
				setval1B(100);
				setval1C(0);
				_delay_ms(1000);
				setval1A(0);
				setval1B(0);
				setval1C(100);
				_delay_ms(1000);
				if(UDR0=='x')
				{
					setval1A(0);
					setval1B(0);
					setval1C(0);
					break;
				}
			}
			break;
			
			
			
			case 't': //disco lights
			
				while(1)
				{
					
					setval1A(100);
					setval1B(100);
					setval1C(0);
					_delay_ms(1000);
					setval1A(0);
					setval1B(100);
					setval1C(100);
					_delay_ms(1000);
					setval1A(100);
					setval1B(0);
					setval1C(100);
					_delay_ms(1000);
					if(UDR0=='x')
					{
						setval1A(0);
						setval1B(0);
						setval1C(0);
						break;
						}
				}
				
				break;
					
			case 'u':    //mode 1
			
				while(1)
				{
					for(i=0;i<101;i++)
					{
					setval1A(i);
					setval1B(i);
					setval1C(i);
					_delay_ms(100);
					}
					for(j=100;j>=0;j--)
					{
						setval1A(j);
						setval1B(j);
						setval1C(j);
						_delay_ms(100);
					}
					if(UDR0=='x')
					{
						setval1A(0);
						setval1B(0);
						setval1C(0);
						break;
					}
				}	
				break;
		
				
	
				}
			}
		return 0;
}