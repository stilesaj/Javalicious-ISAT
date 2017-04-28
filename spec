import static org.junit.Assert.*;

import org.junit.Test;

public class AstrologicalSignTest 
{
	
	@Test
	public void testSignToMonth()
	{
		AstrologicalSign as = new AstrologicalSign(); 
		
		String expectedResult = "Birthday between March 21st and April 19th";
		String actualResult = as.signToMonth("Aries"); 
		assertEquals("Testing that passing the Zodiac sign Ares will return the right string", 
				expectedResult, actualResult);
		
		String expectedString = "Birthday between April 20th and May 20th";
		String actualString = as.signToMonth("Taurus"); 
		assertEquals("Testing that passing the Zodiac sign Taurus will return the right string", 
				expectedString, actualString);
		
		String expString = "Birthday between May 21st and June 20th";
		String actString = as.signToMonth("Gemini"); 
		assertEquals("Testing that passing the Zodiac sign Gemini will return the right string", 
				expString, actString);
		
		String expectedS = "Birthday between June 21st and July 22nd";
		String actualS = as.signToMonth("Cancer"); 
		assertEquals("Testing that passing the Zodiac sign Cancer will return the right string", 
				expectedS, actualS);
		
		String predictedString = "Birthday between July 23rd and August 22nd";
		String outputString = as.signToMonth("Leo"); 
		assertEquals("Testing that passing the Zodiac sign Leo will return the right string", 
				predictedString, outputString);
		
		String predString = "Birthday between August 23rd and October 22nd";
		String outString = as.signToMonth("Virgo"); 
		assertEquals("Testing that passing the Zodiac sign Virgo will return the right string", 
				predString, outString);
		
		String predictedS = "Birthday betwenn October 23rd and Novermber 21st";
		String outputS = as.signToMonth("Scorpio"); 
		assertEquals("Testing that passing the Zodiac sign Scorpio will return the right string", 
				predictedS, outputS);
		
		String guessedString = "Birthday betwenn Novermber 22nd and December 21st";
		String realString = as.signToMonth("Sagittarius"); 
		assertEquals("Testing that passing the Zodiac sign Sagittarius will return the right string", 
				guessedString, realString);
		
		String guessString = "Birthday betwenn December 22nd and January 19th";
		String rString = as.signToMonth("Capricorn"); 
		assertEquals("Testing that passing the Zodiac sign Capricorn will return the right string", 
				guessString, rString);
		
		String guessedS = "Birthday betwenn January 20th and February 18th";
		String realS = as.signToMonth("Aquarius"); 
		assertEquals("Testing that passing the Zodiac sign Aquarius will return the right string", 
				guessedS, realS);
		
		String guessS = "Birthday betwenn February 19th and March 20th";
		String rS = as.signToMonth("Pisces"); 
		assertEquals("Testing that passing the Zodiac sign Pisces will return the right string", 
				guessS, rS);
		
		String expected = "An invalid Zodiac sing was entered";
		String actual = as.signToMonth("ISAT 252"); 
		assertEquals("Testing that passing a random string will return the right string", 
				expected, actual);
	}

}
