import os
import random

from kivy import Config

os.environ["KIVY_NO_CONSOLELOG"] = "1"
cwd = os.getcwd()
os.environ["KIVY_HOME"] = cwd + "/config"
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Config.set("graphics", "width", "800")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", "0")
Config.set("graphics", "borderless", "1")
Config.write()

Builder.load_file("kv-files/main.kv")


class Manager(ScreenManager):
    pass


class Pizza(Screen):
    def pizzaText(self):
        return '''Ingredients
For the base
300g strong bread flour
1 tsp instant yeast (from a sachet or a tub)
1 tsp salt
1 tbsp olive oil, plus extra for drizzling
For the tomato sauce
100ml passata
handful fresh basil or 1 tsp dried
1 garlic clove, crushed
For the topping
125g ball mozzarella, sliced
handful grated or shaved parmesan (or vegetarian alternative)
handful of cherry tomatoes, halved
To finish
handful of basil leaves (optional)'''


class Lasagne(Screen):
    def lasagneRecipe(self):
        return '''Ingredients
2 olive oil, plus a little for the dish
750g lean beef mince
90g pack prosciutto
tomato sauce
200ml hot beef stock
a little grated nutmeg
300g pack fresh lasagne sheets
white sauce
125g ball mozzarella, torn into thin strips'''


class Gyros(Screen):
    def gyrosRecipe(self):
        return '''Ingredients
for 8 servings

2 lb boneless, skinless chicken thighs(910 g), pounded flat
½ large yellow onion, peeled and root side removed
1 wooden skewer, sturdy, roughly 10 inches (25 cm)
MARINADE

2 cups greek yogurt(570 g)
¼ cup lemon juice(60 mL)
¾ cup olive oil(180 mL)
1 tablespoon kosher salt
1 tablespoon garlic, minced
1 tablespoon coriander powder
1 tablespoon paprika
1 tablespoon ground cumin
½ teaspoon cayenne pepper
1 teaspoon cinnamon
1 teaspoon black pepper'''


class Hamburger(Screen):
    def hamburgerRecipe(self):
        return '''Ingredients
1 1/2 pounds 80% lean 20% fat ground beef or ground chuck
1 tablespoon Worcestershire sauce
1 1/2 teaspoons seasoning salt
1 teaspoon garlic powder
1/2 teaspoon ground black pepper
Optional: 4 slices of cheese
4 hamburger buns
Optional: hamburger toppings - lettuce tomato, onion, pickles, ketchup, mustard, mayo, etc.'''


class RecipeWindow(Screen):
    def exit(self):
        RecipeApp().stop()

    def pizzaConsole(self):
        print('''Neapolitan Pizza:
        Pour 700ml of lukewarm water into a large bowl with 10g of sea salt. Gradually mix in a small handful of the 
        flour to break the water and start to turn it into a batter. Mix in the yeast and leave for 2 minutes. 
        Gradually mix in 90% of the remaining flour until you have a pliable, soft dough. 
        Tip the remaining flour on to a clean surface and knead the dough for 20 minutes, or until smooth
         and elastic (or 10 minutes in a free-standing mixer with a dough hook). 
         Place in a floured bowl, cover with a clean damp tea towel and prove for 1 hour, or until doubled in size. 
         Knock out the air with your fists, roll into a sausage shape, 
         chop into 6 equal pieces and roll each one into a ball, stretching the edges underneath. 
         Place on an oiled tray, drizzle with oil, cover with clingfilm and the tea towel 
         and prove overnight in the fridge (for better flavour and a more relaxed dough).

        Preheat the oven to full whack (240ºC/475ºF/gas 9) and place a pizza stone inside. 
        Use a fish slice to move one ball of dough on to a flour-dusted surface. 
        Press the ball out into a fat round disc, then pick it up and gently turn and stretch it to 30cm in diameter,
         using gravity to help you. Stretch it over the back of your fists, then place on a floured pizza paddle
          or board – the dough should be a little thicker around the edges. 
          Pull it into shape and give it a jiggle so you know it’s free-moving. Working quickly and with restraint,
           add your chosen toppings. Quickly shunt on to your pizza stone and close the oven door to retain heat. 
           Wait 7 or 8 minutes and it’ll be golden, crisp and ready to eat.''')

    def lasagneConsole(self):
        print('''Lasagne:
        STEP 1
        To make the meat sauce, heat 2 tbsp olive oil in a frying pan and cook 750g lean beef mince in two batches for about 10 mins
         until browned all over.
        
        STEP 2
        Finely chop 4 slices of prosciutto from a 90g pack, then stir through the meat mixture.
        
        STEP 3
        Pour over 800g passata or half our basic tomato sauce recipe and 200ml hot beef stock. Add a little grated nutmeg, then season.
        
        STEP 4
        Bring up to the boil, then simmer for 30 mins until the sauce looks rich.
        
        STEP 5
        Heat oven to 180C/fan/160C/gas 4 and lightly oil an ovenproof dish (about 30 x 20cm).
        
        STEP 6
        Spoon one third of the meat sauce into the dish, then cover with some fresh lasagne sheets from a 300g pack. 
        Drizzle over roughly 130g ready-made or homemade white sauce.
        
        STEP 7
        Repeat until you have 3 layers of pasta. Cover with the remaining 390g white sauce,
         making sure you can’t see any pasta poking through.
        
        STEP 8
        Scatter 125g torn mozzarella over the top.
        
        STEP 9
        Arrange the rest of the prosciutto on top. Bake for 45 mins until the top is bubbling and lightly browned.''')

    def gyrosConsole(self):
        print('''Gyros:
        Preparation
        In a large bowl, combine marinade ingredients and stir well.
        On a cutting board, place a piece of plastic wrap over the chicken thighs and pound until about ½ inch (1 cm) thick
         with a meat mallet, rolling pin, or heavy pan.
        In another large bowl or gallon plastic bag, combine chicken thighs and marinade, stirring well to coat. 
        Cover and refrigerate for at least one hour and up to one day.
        Preheat oven to 400°F (200°C).
        Shred the cucumber, be sure to squeeze out any excess liquid.
        In a medium bowl, combine tzatziki ingredients and stir well. Cover and refrigerate at least 30 minutes.
        On a baking sheet or a large cast-iron skillet, use the onion half as a base and position the skewer vertically like a spit. 
        Skewer the chicken thighs individually, rotating each one 90 degrees.
        Bake for 1.5 to 2 hours, until internal temperature reaches 165°F (75°C). Let cool for 10 minutes.
        Carve off slices of chicken to fill a pita. Top with onion slices, tomato slices, and tzatziki sauce.
        Enjoy!''')

    def hamburgerConsole(self):
        print('''Hamburger:
            Step 1
            Prepare all your ingredients before you begin. It is important to use mince from a cut of meat that has a little fat. 
            This will not only add flavour, it also ensures a tender burger by preventing the patties from drying out during cooking. 
            However, mince that is too fatty will expel the excess fat during cooking, 
            causing the patties to shrink and toughen considerably. 
            Topside is the recommended mince for making beef burgers as it contains the right amount of fat. Breadcrumbs]
            are not usually included in the traditional burger patty mixture, 
            but their addition to this recipe helps to give the cooked patties a lighter, more tender texture. 
            The egg acts as a binding ingredient so that the patties can be easily shaped. 
            It also helps them hold together when cooked.
            Step 2
            Place the beef mince
            Unsure of the quantity needed?
            Click on the underlined ingredient to reveal the quantity. No need to flip back and forth!
            
            OK, GOT IT
            , breadcrumbs, egg, parsley, onion, garlic, Worcestershire sauce and Tabasco sauce in large bowl. 
            Season with salt and pepper. Mix with your hands until evenly combined.
            Step 3
            Divide the mixture into 6 equal portions (you can use a 125ml / 1/2 cup measuring cup if you like). 
            Shape each portion with your hands into a patty about: 10cm in diameter and 1.5cm thick.
            Step 4
            Place the patties onto a tray lined with- greaseproof paper. 
            Cover with plastic wrap and place in the fridge for at least 30 minutes to rest. 
            Chilling the patties will help them hold together when cooked. 
            This also allows the flavours in the patties to blend and develop. 
            If you chill the patties for any longer, increase the cooking time slightly.
            Step 5
            Heat half the olive oil in a large, non-stick frying pan over medium-low heat 
            and cook half the patties for about 4 minutes on each side or until browned and cooked through. 
            It is important to cook mince right through because it has a larger ratio of surface area 
            to volume than whole pieces of meat, and is therefore at greater risk of contamination by bacteria in the air. 
            Transfer the patties to a plate, set aside and keep warm. Repeat with the remaining oil and patties.
            Step 6
            Meanwhile, preheat grill on high. Place the hamburger buns, cut-side up, 
            under the preheated grill and toast for 1 minute or until golden, as desired. Leave the grill on. 
            Place the patties on a baking tray lined with foil. Top patties with cheese. 
            Place under the grill for 1 minute or until the cheese is just melted.
            Step 7
            To serve, spread the bottom halves of the toasted hamburger buns with the American mustard. 
            Top with the lettuce, sliced tomato, patties and dollop with tomato sauce. Cover with the hamburger bun tops.''')


class RecipeApp(App):
    def build(self):
        self.title = "Recipes"
        return Manager()


RecipeApp().run()
