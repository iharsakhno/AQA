import com.sun.xml.internal.fastinfoset.tools.XML_SAX_StAX_FI;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane;

public class HelloWebDriver {

    public static void main (String[] args) throws InterruptedException {

        WebDriver driver = new ChromeDriver();
        driver.get("https://www.linkedin.com/");
        //driver.manage().window().setSize();
        WebElement searchInput = driver.findElement(By.name("session_key"));
        searchInput.sendKeys("mail");
        WebElement searchInput1 = driver.findElement(By.xpath("/html/body/nav/section[2]/form/div[1]/div[2]/input"));
        searchInput1.sendKeys("password");
        WebElement searchBtn = driver.findElement(By.xpath("/html/body/nav/section[2]/form/div[2]/button"));
        searchBtn.click();
        Thread.sleep(3000);
        WebElement ProfileBtn = driver.findElement(By.id("nav-settings__dropdown-trigger"));
        ProfileBtn.click();
        Thread.sleep(1000);
        WebElement logoutBtn = driver.findElement(By.linkText("Выйти"));
        logoutBtn.click();
        Thread.sleep(2000);
        driver.quit();
       // driver.findElement(By.)
    }
}
