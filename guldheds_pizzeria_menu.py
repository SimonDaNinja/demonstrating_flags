from toppings import Topping

guldheds_pizzeria_menu = {}

guldheds_pizzeria_menu["margherita"] = Topping.TOMATO_SAUCE |\
                                       Topping.CHEESE
margherita = guldheds_pizzeria_menu["margherita"]

guldheds_pizzeria_menu["fungi"] = margherita|\
                                  Topping.CHAMPIGNONS

guldheds_pizzeria_menu["vegetariana"] = margherita |\
                                        Topping.ONION |\
                                        Topping.BELL_PEPPER |\
                                        Topping.OLIVES |\
                                        Topping.ARTICHOKES

guldheds_pizzeria_menu["quatro formagi"] = margherita |\
                                           Topping.MOZARELLA |\
                                           Topping.GORGONZOLA |\
                                           Topping.WHITE_CHEESE |\
                                           Topping.ARUGULA |\
                                           Topping.PESTO

guldheds_pizzeria_menu["prima vera"] = margherita |\
                                       Topping.MOZARELLA |\
                                       Topping.SUN_DRIED_TOMATOES |\
                                       Topping.ARUGULA |\
                                       Topping.PESTO

guldheds_pizzeria_menu["tutti frutti"] = margherita |\
                                         Topping.MOZARELLA |\
                                         Topping.BELL_PEPPER |\
                                         Topping.ARTICHOKES |\
                                         Topping.PINEAPPLE |\
                                         Topping.FRESH_TOMATOES |\
                                         Topping.ARUGULA

guldheds_pizzeria_menu["furitti"] = margherita |\
                                    Topping.BANANA |\
                                    Topping.NUTS |\
                                    Topping.CURRY |\
                                    Topping.PINEAPPLE

furitti = guldheds_pizzeria_menu["furitti"]
chicken_base = margherita | Topping.CHICKEN

guldheds_pizzeria_menu["indiana"] = furitti | chicken_base

guldheds_pizzeria_menu["none special"] = chicken_base |\
                                         Topping.LETTUCE |\
                                         Topping.FRESH_TOMATOES |\
                                         Topping.CUCUMBER |\
                                         Topping.WHITE_CHEESE |\
                                         Topping.FRIGGITELLO |\
                                         Topping.SAUCE

guldheds_pizzeria_menu["kycklingpizza"] = chicken_base |\
                                           Topping.CHAMPIGNONS |\
                                           Topping.ONION |\
                                           Topping.FRESH_TOMATOES |\
                                           Topping.FRIGGITELLO |\
                                           Topping.SAUCE

guldheds_pizzeria_menu["capri"] = margherita |\
                                  Topping.GROUND_MEAT

capri = guldheds_pizzeria_menu["capri"]

guldheds_pizzeria_menu["cannibale"] = capri |\
                                      Topping.HAM |\
                                      Topping.ONION

guldheds_pizzeria_menu["orientale"] = capri |\
                                      Topping.ONION |\
                                      Topping.FRESH_TOMATOES |\
                                      Topping.GARLIC |\
                                      Topping.PIRI_PIRI

guldheds_pizzeria_menu["mafioso"] = capri |\
                                    Topping.HAM |\
                                    Topping.BACON |\
                                    Topping.ONION |\
                                    Topping.EGGS

guldheds_pizzeria_menu["mexicana"] = capri |\
                                     Topping.ONION |\
                                     Topping.BELL_PEPPER |\
                                     Topping.JALAPENOS |\
                                     Topping.FRIGGITELLO

guldheds_pizzeria_menu["matera"] = capri |\
                                   Topping.ONION |\
                                   Topping.CHAMPIGNONS |\
                                   Topping.BELL_PEPPER |\
                                   Topping.GORGONZOLA

guldheds_pizzeria_menu["henkes favorit"] = capri |\
                                           Topping.HAM |\
                                           Topping.SALAMI |\
                                           Topping.ONION |\
                                           Topping.PINEAPPLE

guldheds_pizzeria_menu["trakya"] = capri |\
                                   Topping.SALAMI |\
                                   Topping.BACON |\
                                   Topping.SAUCE

kebab_base = margherita | Topping.KEBAB_MEAT

guldheds_pizzeria_menu["skeppet"] = kebab_base |\
                                    Topping.FRESH_TOMATOES |\
                                    Topping.WHITE_CHEESE |\
                                    Topping.GARLIC_SAUCE

guldheds_pizzeria_menu["kebabpizza"] = kebab_base |\
                                       Topping.CHAMPIGNONS |\
                                       Topping.ONION

guldheds_pizzeria_menu["amhult"] = kebab_base |\
                                   Topping.HAM |\
                                   Topping.SAUCE

guldheds_pizzeria_menu["p99"] = kebab_base |\
                                Topping.FRIES |\
                                Topping.SAUCE

guldheds_pizzeria_menu["bagarens special"] = kebab_base |\
                                             Topping.LETTUCE |\
                                             Topping.CUCUMBER |\
                                             Topping.FRESH_TOMATOES |\
                                             Topping.WHITE_CHEESE |\
                                             Topping.FRIGGITELLO |\
                                             Topping.SAUCE

guldheds_pizzeria_menu["grabbarnas special"] = kebab_base |\
                                               Topping.BACON |\
                                               Topping.FRESH_TOMATOES |\
                                               Topping.ONION |\
                                               Topping.WHITE_CHEESE |\
                                               Topping.SAUCE

oxfile_base = margherita | Topping.BEEF_TENDERLOIN

guldheds_pizzeria_menu["milano"] = oxfile_base |\
                                   Topping.GROUND_MEAT |\
                                   Topping.FRESH_TOMATOES |\
                                   Topping.ONION |\
                                   Topping.WHITE_CHEESE |\
                                   Topping.ARUGULA |\
                                   Topping.PESTO

guldheds_pizzeria_menu["automeca special"] = oxfile_base |\
                                             Topping.GROUND_MEAT |\
                                             Topping.CHAMPIGNONS |\
                                             Topping.SAUCE

guldheds_pizzeria_menu["bella mia"] = oxfile_base |\
                                      Topping.HAM |\
                                      Topping.BEARNAISE_SAUCE

guldheds_pizzeria_menu["reale"] = oxfile_base |\
                                  Topping.EGGS |\
                                  Topping.BEARNAISE_SAUCE

guldheds_pizzeria_menu["ciao ciao"] = oxfile_base |\
                                      Topping.CHAMPIGNONS |\
                                      Topping.ONION |\
                                      Topping.GARLIC

guldheds_pizzeria_menu["de lux"] = oxfile_base |\
                                   Topping.ONION |\
                                   Topping.GORGONZOLA |\
                                   Topping.FRESH_TOMATOES |\
                                   Topping.GARLIC

guldheds_pizzeria_menu["africana"] = oxfile_base |\
                                     Topping.PINEAPPLE |\
                                     Topping.NUTS |\
                                     Topping.CURRY

guldheds_pizzeria_menu["nobile"] = oxfile_base |\
                                   Topping.BELL_PEPPER |\
                                   Topping.FRESH_TOMATOES |\
                                   Topping.JALAPENOS |\
                                   Topping.ONION |\
                                   Topping.ONION

guldheds_pizzeria_menu["jägare"] = oxfile_base |\
                                   Topping.HAM |\
                                   Topping.BACON |\
                                   Topping.GROUND_MEAT |\
                                   Topping.ONION |\
                                   Topping.GARLIC

guldheds_pizzeria_menu["acpolco"] = oxfile_base |\
                                    Topping.JALAPENOS |\
                                    Topping.ONION |\
                                    Topping.TACO_SAUCE

stark_korv_base = margherita | Topping.SPICY_SAUSAGE

guldheds_pizzeria_menu["beritan"] = stark_korv_base |\
                                    Topping.FRIGGITELLO |\
                                    Topping.FRESH_TOMATOES

guldheds_pizzeria_menu["raman special"] = stark_korv_base |\
                                          Topping.CHAMPIGNONS |\
                                          Topping.ONION

guldheds_pizzeria_menu["ravin"] = stark_korv_base |\
                                  Topping.HAM

mozarella_base = margherita | Topping.MOZARELLA

guldheds_pizzeria_menu["buttana"] = mozarella_base |\
                                    Topping.ITALIAN_DI_PARMA |\
                                    Topping.GORGONZOLA |\
                                    Topping.ARUGULA |\
                                    Topping.GARLIC

guldheds_pizzeria_menu["frateli"] = mozarella_base |\
                                    Topping.ITALIAN_DI_PARMA |\
                                    Topping.ARUGULA |\
                                    Topping.PESTO

guldheds_pizzeria_menu["inter"] = mozarella_base |\
                                  Topping.ITALIAN_DI_PARMA |\
                                  Topping.BELL_PEPPER |\
                                  Topping.SUN_DRIED_TOMATOES |\
                                  Topping.ARUGULA |\
                                  Topping.GARLIC

guldheds_pizzeria_menu["porto"] = mozarella_base |\
                                  Topping.ITALIAN_DI_PARMA |\
                                  Topping.CHAMPIGNONS |\
                                  Topping.ARUGULA |\
                                  Topping.PESTO

guldheds_pizzeria_menu["marco polo"] = mozarella_base |\
                                       Topping.ITALIAN_DI_PARMA |\
                                       Topping.ARTICHOKES |\
                                       Topping.SUN_DRIED_TOMATOES |\
                                       Topping.GREEK_OLIVES |\
                                       Topping.ARUGULA |\
                                       Topping.PESTO

guldheds_pizzeria_menu["pelpis special"] = mozarella_base |\
                                           Topping.BEEF_TENDERLOIN |\
                                           Topping.GROUND_MEAT |\
                                           Topping.ONION |\
                                           Topping.BELL_PEPPER |\
                                           Topping.WHITE_CHEESE |\
                                           Topping.ARUGULA |\
                                           Topping.PESTO

ham_base = margherita | Topping.HAM

guldheds_pizzeria_menu["prosciutto"] = ham_base

guldheds_pizzeria_menu["calzone"] = ham_base

guldheds_pizzeria_menu["hawaii"] = ham_base | Topping.PINEAPPLE

guldheds_pizzeria_menu["capricciosa"] = ham_base | Topping.CHAMPIGNONS

guldheds_pizzeria_menu["super mario"] = ham_base |\
                                        Topping.FRIES |\
                                        Topping.SAUCE

guldheds_pizzeria_menu["salami"] = ham_base |\
                                   Topping.SALAMI |\
                                   Topping.ONION |\
                                   Topping.FRESH_TOMATOES |\
                                   Topping.OLIVES

guldheds_pizzeria_menu["tropical"] = ham_base |\
                                     Topping.BANANA |\
                                     Topping.PINEAPPLE

guldheds_pizzeria_menu["bella"] = margherita |\
                                  Topping.CHAMPIGNONS |\
                                  Topping.SHRIMP

guldheds_pizzeria_menu["pascatore"] = margherita |\
                                      Topping.SHRIMP |\
                                      Topping.TUNA

guldheds_pizzeria_menu["venezia"] = margherita |\
                                    Topping.HAM |\
                                    Topping.TUNA

guldheds_pizzeria_menu["tomaso"] = margherita |\
                                   Topping.HAM |\
                                   Topping.SHRIMP

guldheds_pizzeria_menu["marinara"] = margherita |\
                                     Topping.SHRIMP |\
                                     Topping.MUSSELS

guldheds_pizzeria_menu["prinsessa"] = margherita |\
                                      Topping.HAM |\
                                      Topping.PINEAPPLE |\
                                      Topping.SHRIMP

guldheds_pizzeria_menu["quattro stagioni"] = margherita |\
                                             Topping.HAM |\
                                             Topping.CHAMPIGNONS |\
                                             Topping.SHRIMP |\
                                             Topping.ARTICHOKES

guldheds_pizzeria_menu["havets special"] = margherita |\
                                           Topping.CRAYFISH_TAILS |\
                                           Topping.GARLIC |\
                                           Topping.SHRIMP |\
                                           Topping.PIRI_PIRI

