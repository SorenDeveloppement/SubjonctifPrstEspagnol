import asyncio
from pyppeteer import launch

verbs = ["andar", "caber", "caer", "conducir", "decir", "estar", "hacer", "ir", "oir", "poner", "saber", "salir", "ser",
         "tener", "traer", "valer", "venir", "ver"]
prefix = None


async def main():
    global prefix
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.elconjugador.com/')

    with open("subjonctif_verbs.txt", "w") as file:
        for verb in verbs:
            await page.type("#v", verb + "\r")

            file.write(verb + "\r")
            prefix = verb[:len(verb)-2]
            for i in range(2, 14, 2):
                elem = await page.J(f"body > section > main > div:nth-child(20) > b:nth-child({i})")
                file.write(str(prefix) + await page.evaluate("(elem) => elem.textContent", elem) + "\r")

            file.write("-------------------------------------------------------\r")
        file.close()

    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
