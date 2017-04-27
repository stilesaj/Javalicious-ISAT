//A program to determine where your birthday may lie on a calendar according to your zodiac sign
public class AstrologicalSign 
{
	public String signToMonth(String sign)
	{
		String returnValue; 
//switches which return values that state birthday ranges based on zodiac signs		
		switch(sign)
		{
			case "Aries":
			returnValue = "Birthday between March 21st and April 19th";
			break;
			
			case"Taurus":
			returnValue = "Birthday between April 20th and May 20th";
			break; 
			
			case"Gemini":
			returnValue = "Birthday between May 21st and June 20th";
			break;
			
			case"Cancer":
			returnValue = "Birthday between June 21st and July 22nd";
			break;
			
			case"Leo":
			returnValue = "Birthday between July 23rd and August 22nd";
			break;
			
			case"Virgo":
			returnValue = "Birthday between August 23rd and October 22nd";
			break;
			
			case"Scorpio":
			returnValue = "Birthday betwenn October 23rd and Novermber 21st"; 
			break; 
			
			case"Sagittarius":
			returnValue = "Birthday betwenn Novermber 22nd and December 21st"; 
			break;
			
			case"Capricorn":
			returnValue = "Birthday betwenn December 22nd and January 19th"; 
			break;
			
			case"Aquarius":
			returnValue = "Birthday betwenn January 20th and February 18th"; 
			break;
			
			case"Pisces":
			returnValue = "Birthday betwenn February 19th and March 20th"; 
			break;
	//If the user didn't insert a correct zodiac sign from the switches above, the default return value will be given below:		
			default:
			returnValue = "An invalid Zodiac sing was entered";
		}
		
		return returnValue; 
	}
}
