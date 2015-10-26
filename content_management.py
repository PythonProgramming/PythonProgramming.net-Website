##
##//
##
##
##// CURRENT:
##// list of topics by {TOPIC:[["TITLE", "URL"]]}
##
##// FUTURE:
##////list of topics by {TOPIC:[["TITLE", "URL", "TAGS"],
##////                          ["TITLE", "URL", "TAGS"]]}






def Content():
##    //             Suggest Branches for next steps
##    //             If liked: Matplotlib, link to data analysis or Pandas maybe
##    //             If liked: GUI stuff: Kivy, PyGame, Tkinter
##    //             if liked: Text and word-based: NLTK


    # MAIN : [TITLE, URL, BODY_TEXT (LIST), HINTS(LIST)]
    TOPIC_DICT = {"Basics":[["Python Introduction","/introduction-to-python-programming/",[""]],
                            ["Print Function and Strings","/python-tutorial-print-function-strings/",["The Print function outputs text to the console (black area). Let's try it out!","print() is a function, which does something with parameters, and parameters go inside the parenthesis.","See if you can use the print function to output 'Hello!' to the console!"]],
                            ["Math with Python","/math-basics-python-3-beginner-tutorial/"],
                            ["Variables","/python-3-variables-tutorial/"],
                            ["While Loop","/python-3-loop-tutorial/"],
                            ["For Loop","/loop-python-3-basics-tutorial/"],
                            ["If Statement","/if-statement-python-3-basics-tutorial/"],
                            ["If Else","/else-python-3-tutorial/"],
                            ["If Elif Else","/elif-else-python-3-tutorial/"],
                            ["Functions","/functions-python-3-basics-tutorial/"],
                            ["Function Parameters","/function-parameters-python-3-basics/"],
                            ["Function Parameter Defaults","/function-parameter-defaults-python-3-basics/"],
                            ["Global and Local Variables","/global-local-variables/"],
                            ["Installing Modules","/installing-modules-python-3/"],
                            ["How to download and install Python Packages and Modules with Pip ","/using-pip-install-for-python-modules/"],
                            ["Common Errors","/common-errors-python-3-basics/"],
                            ["Writing to a File","/writing-file-python-3-basics/"],
                            ["Appending Files","/appending-file-python-3-tutorial/"],
                            ["Reading from Files","/reading-file-python-3-tutorial/"],
                            ["Classes","/classes-python-3-basics-tutorial/"],
                            ["Frequently asked Questions","/frequently-asked-questions-python-3/"],
                            ["Getting User Input","/user-input-python-3-tutorial/"],
                            ["Statistics Module","/statistics-python-3-module-mean-standard-deviation/"],
                            ["Module import Syntax","/module-import-syntax-python-3-tutorial/"],
                            ["Making your own Modules","/making-modules/"],
                            ["Python Lists vs Tuples","/python-lists-vs-tuples/"],
                            ["List Manipulation","/python-3-list-manipulation/"],
                            ["Multi-dimensional lists","/python-3-multi-dimensional-list/"],
                            ["Reading CSV files in Python","/reading-csv-files-python-3/"],
                            ["Try and Except Error handling","/handling-exceptions-try-except-python-3/"],
                            ["Multi-Line printing","/multi-line-printing-python-3/"],
                            ["Python dictionaries","/dictionaries-tutorial-python-3/"],
                            ["Built in functions","/built-functions-python-3/"],
                            ["OS Module","/python-3-os-module/"],
                            ["SYS module","/sys-module-python-3/"],
                            ["Python urllib tutorial for Accessing the Internet","/urllib-tutorial-python-3/"],
                            ["Regular Expressions with re","/regular-expressions-regex-tutorial-python-3/"],
                            ["How to Parse a Website with regex and urllib","/parse-website-using-regular-expressions-urllib/"],
                            ["Tkinter intro","/python-3-tkinter-basics-tutorial/"],
                            ["Tkinter buttons","/tkinter-python-3-tutorial-adding-buttons/"],
                            ["Tkinter event handling","/tkinter-tutorial-python-3-event-handling/"],
                            ["Tkinter menu bar","/tkinter-menu-bar-tutorial/"],
                            ["Tkinter images, text, and conclusion","/tkinter-adding-text-images/"],
                            ["Threading module","/threading-tutorial-python/"],
                            ["CX_Freeze","/converting-python-scripts-exe-executables/"],
                            ["The Subprocess Module","/python-3-subprocess-tutorial/"],
                            ["Matplotlib Crash Course","/matplotlib-python-3-basics-tutorial/"],
                            ["Python ftplib Tutorial","/ftp-transfers-python-ftplib/"],
                            ["Sockets with Python Intro","/python-sockets/"],
                            ["Simple Port Scanner with Sockets","/python-port-scanner-sockets/"],
                            ["Threaded Port Scanner","/python-threaded-port-scanner/"],
                            ["Binding and Listening with Sockets","/python-binding-listening-sockets/"],
                            ["Client Server System with Sockets","/client-server-python-sockets/"],
                            ["Python 2to3 for Converting Python 2 scripts to Python 3","/converting-python2-to-python3-2to3/"]],
                  
                  "PyGame":[["Introduction to PyGame","/pygame-python-3-part-1-intro/"],
                            ["Displaying images with PyGame","/displaying-images-pygame/"],
                            ["Moving an image around in PyGame","/pygame-tutorial-moving-images-key-input/"],
                            ["Adding boundaries","/adding-boundaries-pygame-video-game/"],
                            ["Displaying text to PyGame screen","/displaying-text-pygame-screen/"],
                            ["Drawing objects with PyGame","/drawing-objects-pygame-tutorial/"],
                            ["Crashing","/pygame-crashing-objects/"],
                            ["PyGame Score","/adding-score-pygame-video-game/"],
                            ["Drawing Objects and Shapes in PyGame","/pygame-drawing-shapes-objects/"],
                            ["Creating a start menu","/pygame-start-menu-tutorial/"],
                            ["PyGame Buttons, part 1, drawing the rectangle","/pygame-buttons-part-1-button-rectangle/"],
                            ["PyGame Buttons, part 2, making the buttons interactive","/making-interactive-pygame-buttons/"],
                            ["PyGame Buttons, part 3, adding text to the button","/placing-text-pygame-buttons/"],
                            ["PyGame Buttons, part 4, creating a general PyGame button function","/pygame-button-function/"],
                            ["PyGame Buttons, part 5, running functions on a button click","/pygame-button-function-events/"],
                            ["Converting PyGame to an executable","/converting-pygame-executable-cx_freeze/"],
                            ["Adding a pause function to our game and Game Over","/pause-game-pygame/"],
                            ["PyGame Icon","/changing-pygame-icon/"],
                            ["Sounds and Music with PyGame","/adding-sounds-music-pygame/"],],




                  
                  "PyOpenGL":[["OpenGL with PyOpenGL introduction and creation of Rotating Cube","/opengl-rotating-cube-example-pyopengl-tutorial/"],
                              ["Coloring Surfaces as well as understand some of the basic OpenGL code","/coloring-pyopengl-surfaces-python-opengl/"],
                              ["Understanding navigation within the 3D environment via OpenGL","/navigating-3d-environment/"],
                              ["Moving the player automatically towards the cube","/moving-towards-pyopengl-cube/"],
                              ["Random Cube Position","/random-cube-position-pyopengl-tutorial/"],
                              ["Adding Many Cubes to our Game","/multiple-opengl-cubes/"],
                              ["Adding a ground in OpenGL","/adding-ground-pyopengl-tutorial/"],
                              ["Infinite flying cubes","/infinite-3d-pyopengl-flying-cubes-tutorial/"],
                              ["Optimizing the processing for infinite cubes","/improving-infinite-3d-cubes-pyopengl-tutorial/"],],

                  
                  "Kivy":[["Kivy with Python tutorial for Mobile Application Development Part 1","/kivy-application-development-tutorial/"],
                          ["Kivy Widgets and Labels","/kivy-widgets-labels/"],
                          ["The Kivy .kv Language","/kivy-language-tutorial/"],
                          ["Kivy .kv Language cont'd","/more-kivy-language/"],
                          ["Dynamic Resizable Placement","/dynamic-kivy-content-placement/"],
                          ["Layouts: Float Layout","/kivy-float-layout/"],
                          ["Getting Mouse / Press / Touch Input","/getting-mouse-press-touch-input-kivy/"],
                          ["Simple Drawing Application","/kivy-drawing-application-tutorial/"],
                          ["Builder for loading .kv Files","/kivy-loader-for-style/"],
                          ["Screen Manager for Multiple Screens","/kivy-screen-manager-tutorial/"],
                          ["Drawing Application with Screen Manager","/drawing-application-with-screen-manager/"],
                          ["Adding better Navigation","/kivy-application-navigation/"],],

                  "PyQt":[["PyQt Tutorials coming soon!","/pyqt-python-programming-tutorials/"],],

                  "Finance":[["Section under construction","/under-construction/"],],


                  
                  "Flask":[["Intro and environment creation","/flask-web-development-introduction/"],
                           ["Basics, init.py, and your first Flask App!","/creating-first-flask-web-app/"],
                           ["Incorporating Variables and some Logic","/templates-flask-variables-html/"],
                           ["Using Bootstrap to make things pretty","/flask-bootstrap/"],
                           ["Using javascript plugins, with a Highcharts example","/adding-js-plugins-flask-highcharts-example/"],
                           ["Incorporating extends for templates","/flask-template-extends/"],],

                  
                  "Django":[["Django Development Videos","/python-web-development-django/"],],


                  
                  "MySQL":[["Intro to MySQL","/mysql-intro/"],
                           ["Creating Tables and Inserting Data with MySQL","/create-mysql-tables-insert/"],
                           ["Update, Select, and Delete with MySQL","/mysql-update-select-delete/"],
                           ["Inserting Variable Data with MySQL","/mysql-insert-variable/"],
                           ["Streaming Tweets from Twitter to Database","/mysql-live-database-example-streaming-data/"],],

                  
                  "SQLite":[["Inserting into a Database with SQLite","/sql-database-python-part-1-inserting-database/"],
                            ["Dynamically Inserting into a Database with SQLite","/sqlite-part-2-dynamically-inserting-database-timestamps/"],
                            ["Read from Database with SQLite","/sqlite-part-3-reading-database-python/"],
                            ["Graphing example from SQLite","/graphing-from-sqlite-database/"],],

                  
                  "Data Manipulation":[["Intro to Pandas and Saving to a CSV and reading from a CSV","/pandas-saving-reading-csv-file/"],
                                       ["Pandas Column manipulation","/pandas-column-manipulation-spreadsheet-data/"],
                                       ["Pandas Column Operations (basic math operations and moving averages)","/pandas-column-operations-calculations/"],
                                       ["Pandas 2D Visualization of Pandas data with Matplotlib, including plotting dates","/2D-Visualization-of-Pandas-data-with-Matplotlib-including-plotting-dates/"],
                                       ["Pandas 3D Visualization of Pandas data with Matplotlib","/3d-graphing-pandas-matplotlib/"],
                                       ["Pandas Standard Deviation","/pandas-standard-deviation/"],
                                       ["Pandas Correlation matrix and Statistics Information on Data","/pandas-statistics-correlation-tables-how-to/"],
                                       ["Pandas Function mapping for advanced Pandas users","/python-function-mapping-pandas/"],],

                  
                  "Data Visualization":[["Matplotlib Crash Course","/matplotlib-python-3-basics-tutorial/"],
                                        ["3D graphs in Matplotlib","/3d-graphing-python-matplotlib/"],
                                        ["3D Scatter Plot with Python and Matplotlib","/matplotlib-3d-scatterplot-tutorial/"],
                                        ["More 3D scatter-plotting with custom colors","/3d-scatter-plot-customizing/"],
                                        ["3D Barcharts","/3d-bar-charts-python-matplotlib/"],
                                        ["3D Plane wireframe Graph","/wireframe-graph-python/"],
                                        ["Live Updating Graphs with Matplotlib Tutorial","/python-matplotlib-live-updating-graphs/"],
                                        ["Modify Data Granularity for Graphing Data","/modifying-data-granularity-matplotlib/"],
                                        ["Geographical Plotting with Basemap and Python p. 1","/geographical-plotting-basemap-tutorial/"],
                                        ["Geographical Plotting with Basemap and Python p. 2","/map-plotting-basemap-matplotlib-part-2/"],
                                        ["Geographical Plotting with Basemap and Python p. 3","/basemap-possibilities/"],
                                        ["Geographical Plotting with Basemap and Python p. 4","/plotting-maps-python-basemap/"],
                                        ["Geographical Plotting with Basemap and Python p. 5","/basemap-python-plotting-tutorial-part-5/"],
                                        ["Advanced Matplotlib Series (videos and ending source only)","/advanced-matplotlib-graphing-charting-tutorial/"],],


                  
                  "Natural Language Processing with NLTK":[["Simple RSS feed scraping","/scraping-parsing-rss-feed/"],
                                                                        ["Simple website scraping","/scraping-text-websites/"],
                                                                        ["More Parsing/Scraping","/website-scraping-basics/"],
                                                                        ["Installing the Natural Language Toolkit (NLTK)","/installing-nltk-nlp-python/"],
                                                                        ["NLTK Part of Speech Tagging Tutorial","/natural-language-toolkit-nltk-part-speech-tagging/"],
                                                                        ["Named Entity Recognition NLTK tutorial","/named-entity-recognition-nltk-python/"],
                                                                        
                                                                        ["Building a Knowledge-base","/building-nlp-knowledge-base/"],
                                                                        ["More Named Entity Recognition with NLTK","/more-named-entity-recognition/"],
                                                                        ["Pulling related Sentiment about Named Entities","/finding-related-sentiment/"],
                                                                        ["Populating a knowledge-base","/populating-nlp-database/"],
                                                                        ["What next?","/what-next-nlp-tutorial/"],
                                                                        ["Accuracy Testing","/accuracy-testing-basic-nlp/"],
                                                                        ["Building back-testing","/back-testing-nlp-nltk/"],
                                                                        ["Machine learning and Sentiment Analysis","/learning-for-sentiment-analysis/"],],

                  
                  "Support Vector Machines (SVM)":[["Intro to Machine Learning with Scikit Learn and Python","/machine-learning-python-sklearn-intro/"],
                                                   ["Simple Support Vector Machine (SVM) example with character recognition","/support-vector-machine-svm-example-tutorial-scikit-learn-python/"],
                                                   ["Our Method and where we will be getting our Data","/data-acquisition-machine-learning/"],
                                                   ["Parsing data","/getting-data-machine-learning/"],
                                                   ["More Parsing","/parsing-data-website-machine-learning/"],
                                                   ["Structuring data with Pandas","/using-pandas-structure-process-data/"],
                                                   ["Getting more data and meshing data sets","/getting-data-sp-500-index-value-comparison/"],
                                                   ["Labeling of data part 1","/labeling-data-machine-learning/"],
                                                   ["Labeling data part 2","/labeling-data-machine-learning-part-2/"],
                                                   ["Finally finishing up the labeling","/label-data-machine-learning/"],
                                                   ["Linear SVC Machine learning SVM example with Python","/linear-svc-example-scikit-learn-svm-python/"],
                                                   ["Getting more features from our data","/collecting-features-machine-learning/"],
                                                   ["Linear SVC machine learning and testing our data","/linear-svc-machine-learning-testing-data/"],
                                                   ["Scaling, Normalizing, and machine learning with many features","/preprocessing-machine-learning/"],
                                                   ["Shuffling our data to solve a learning issue","/shuffling-data-learning/"],
                                                   ["Using Quandl for more data","/using-quandl-data/"],
                                                   ["Improving our Analysis with a more accurate measure of performance in relation to fundamentals","/improving-analysis-machine-learning/"],
                                                   ["Learning and Testing our Machine learning algorithm","/learning-and-testing-svm/"],
                                                   ["More testing, this time including N/A data","/machine-learning-testing-with-na/"],
                                                   ["Back-testing the strategy","/back-testing-machine-learning-investing-strategy/"],
                                                   ["Pulling current data from Yahoo","/current-yahoo-data-for-machine-learning/"],
                                                   ["Building our New Data-set","/building-yahoo-data-machine-learning/"],
                                                   ["Searching for investment suggestions","/investment-suggestions-machine-learning/"],
                                                   ["Raising investment requirement standards","/raising-investment-suggestion-requirements/"],
                                                   ["Testing raised standards","/machine-learning-testing-new-algo/"],
                                                   ["Streamlining the changing of standards","/streamlining-changing-machine-learning/"],],


                  
                  "Clustering (unsupervised learning)":[["Unsupervised Machine Learning: Flat Clustering","/flat-clustering-machine-learning-python-scikit-learn/"],
                                                        ["Unsupervised Machine Learning: Hierarchical Clustering","/hierarchical-clustering-machine-learning-python-scikit-learn/"],],
                  
                  "Image Recognition":[["Introduction and Dependencies","/image-recognition-python/"],
                                       ["Understanding Pixel Arrays","/python-pixel-arrays/"],
                                       ["More Pixel Arrays","/more-pixel-arrays/"],
                                       ["Graphing our images in Matplotlib","/graphing-images-matplotlib/"],
                                       ["Thresholding","/image-thresholding-python/"],
                                       ["Thresholding Function","/thresholding-python-function/"],
                                       ["Thresholding Logic","/automated-image-thresholding-python/"],
                                       ["Saving our Data For Training and Testing","/saving-image-data/"],
                                       ["Basic Testing","/basic-image-recognition-testing/"],
                                       ["Testing, visualization, and moving forward","/testing-visualization-and-conclusion/"],],


                  
                  "Forex Algo HFT":[["Introduction","/machine-learning-pattern-recognition-algorithmic-forex-stock-trading/"],
                                    ["Quick Look at our Data","/pattern-recognition-dataset/"],
                                    ["Basics","/forex-algo-pattern-rec-basics/"],
                                    ["Percent Change","/percent-change-python/"],
                                    ["Finding Patterns","/finding-forex-algo-patterns/"],
                                    ["Storing Patterns","/storing-found-patterns/"],
                                    ["Current Pattern","/recognizing-current-pattern/"],
                                    ["Predicting outcomes","/predicting-outcomes-of-patterns/"],
                                    ["More predicting","/more-predicting-outcomes/"],
                                    ["Increasing pattern complexity","/increasing-pattern-complexity/"],
                                    ["More on Patterns","/more-on-patterns-hft-forex/"],
                                    ["Displaying all patterns","/displaying-our-forex-patterns/"],
                                    ["Variables in patterns","/variables-in-forex-patterns/"],
                                    ["Past outcomes as possible predictions","/past-pattern-outcomes-predictions/"],
                                    ["Predicting from patterns","/predicting-from-patterns/"],
                                    ["Average outcomes as predictions","/average-outcomes-as-predictions-forex-hft/"],],


                  
                  "Robotics with the Raspberry Pi":[["Robotics with the Raspberry Pi","/robot-remote-control-car-with-the-raspberry-pi/"],
                                                    ["Programming GPIO example","/gpio-example-raspberry-pi/"],
                                               ["Running GPIO","/running-gpio-python-raspberry-pi/"],
                                               ["Building Autonomous / RC car intro","/gpio-raspberry-pi-car-intro/"],
                                               ["Supplies needed","/raspberry-pi-car-supplies/"],
                                               ["Motor Control","/gpio-motor-control-raspberry-pi/"],
                                               ["Connecting the four motors","/connecting-motors-raspberry-pi/"],
                                               ["Forward and Reverse","/forward-reverse-motors-raspberry-pi/"],
                                               ["Turning","/turning-raspberry-pi-car/"],
                                               ["Pivoting","/pivoting-raspberry-pi-car/"],
                                               ["User Control","/user-control-raspberry-pi-car/"],
                                               ["Remotely controlling the car","/raspberry-pi-car-remote-control/"],
                                               ["Adding a distance sensor (HC-SR04)","/raspberry-pi-car-distance-sensor/"],
                                               ["Programming with the distance sensor","/raspberry-pi-hc-sr04-programming/"],
                                               ["Autopilot and/or auto-correct","/autopilot-raspberry-pi-car/"],
                                               ["Autonomous Beginnings","/autonomous-raspberry-pi-car/"],
                                               ["Testing Autonomous Code","/testing-autonomous-raspberry-pi-car/"],
                                               ["Streaming video example one","/streaming-video-from-raspberry-pi-camera/"],
                                               ["Less latency streaming option","/low-latency-video-streaming-raspberry-pi/"],],

                  
                  "Build a Supercomputer and program with MPI":[["Build a Supercomputer with Raspberry Pis","/build-supercomputer-raspberry-pi/"],
                                                                ["Intro","/supercomputer-intro/"],
                                                                ["Supplies","/supplies-for-supercomputer/"],
                                                                ["Installing Operating System","/installing-supercomputer-operating-system/"],
                                                                ["Downloading and installing MPI","/download-and-install-mpi-for-supercomputer/"],
                                                                ["Testing Supercomputer","/testing-supercomputer/"],
                                                                
                                                                ["MPI with MPI4py Introduction","/learning-use-mpi-python-mpi4py-module/"],
                                                                ["Installing mpi4py for use with Python and MPI","/installing-testing-mpi4py-mpi-python-tutorial/"],
                                                                ["First basic MPI script with mpi4py","/basic-mpi4py-script-getting-node-rank/"],
                                                                ["Using  conditional, Python, statements alongside MPI commands example","/conditional-statements-alongside-mpi-mpi4py/"],
                                                                ["Getting network processor size with the size command","/mpi4py-size-command-mpi/"],
                                                                ["Sending and Receiving data using send and recv commands with MPI","/sending-receiving-data-messages-mpi4py/"],
                                                                ["Dynamically sending messages to and from processors with MPI and mpi4py","/sending-receiving-messages-nodes-dynamically/"],
                                                                ["Message and data tagging for send and recv MPI commands tutorial","/tagging-messages-mpi-multiple-messages/"],
                                                                ["MPI broadcasting tutorial with Python, mpi4py, and bcast","/mpi-broadcast-tutorial-mpi4py/"],
                                                                ["Scatter with MPI tutorial with mpi4py","/scatter-gather-mpi-mpi4py-tutorial/"],
                                                                ["Gather command with MPI, mpi4py, and Python","/mpi-gather-command-mpi4py-python/"],],



                  
                  "Tkinter":[["Programming GUIs and windows with Tkinter and Python Introduction ","/tkinter-depth-tutorial-making-actual-program/"],
                             ["Object Oriented Programming Crash Course with Tkinter","/object-oriented-programming-crash-course-tkinter/"],
                             ["Passing functions with Parameters in Tkinter using Lambda","/passing-functions-parameters-tkinter-using-lambda/"],
                             ["How to change and show a new window in Tkinter","/change-show-new-frame-tkinter/"],
                             ["Styling your GUI a bit using TTK","/styling-gui-bit-using-ttk/"],
                             ["How to embed a Matplotlib graph to your Tkinter GUI","/how-to-embed-matplotlib-graph-tkinter-gui/"],
                             ["How to make the Matplotlib graph live in your application","/embedding-live-matplotlib-graph-tkinter-gui/"],
                             ["Organizing our GUI","/organizing-gui/"],
                             ["Plotting Live Updating Data in Matplotlib and our Tkinter GUI","/plotting-live-bitcoin-price-data-tkinter-matplotlib/"],
                             ["Customizing an embedded Matplotlib Graph in Tkinter","/customizing-tkinter-matplotlib-graph/"],
                             ["Creating our Main Menu in Tkinter","/creating-main-menu-tkinter/"],
                             ["Building a pop-up message window","/tkinter-popup-message-window/"],
                             ["Exchange Choice Option","/adding-tkinter-menu-options/"],
                             ["Time-frame and sample size option","/time-frame-sample-size-options/"],
                             ["Adding indicator Menus (3 videos)","/adding-indicator-choice-menu/"],
                             ["Trading option, start/stop, and help menu options","/adding-trading-option/"],
                             ["Tutorial on adding a tutorial","/tutorial-for-tkinter-tutorial/"],
                             ["Allowing the exchange choice option to affect actual shown exchange","/exchange-choice-handling/"],
                             ["Adding exchange choice cont'd","/adding-exchanges-2/"],
                             ["Adding exchange choices part 3","/adding-exchanges-3/"],
                             ["Indicator Support","/adding-indicator-support/"],
                             ["Pulling data from the Sea of BTC API","/pulling-data-from-seaofbtc/"],
                             ["Setting up sub plots within our Tkinter GUI","/subplots-within-tkinter-gui/"],
                             ["Graphing an OHLC candlestick graph embedded in our Tkinter GUI","/graphing-ohlc-candlestick-in-tkinter/"],
                             ["Acquiring RSI data from Sea of BTC API","/getting-rsi-data-for-tkinter-gui/"],
                             ["Acquiring MACD data from Sea of BTC API","/getting-macd-data-for-tkinter-gui/"],
                             ["Converting Tkinter application to .exe and installer with cx_Freeze","/converting-tkinter-to-exe-with-cx-freeze/"],],





                  "Python and Pandas with Sentiment Analysis Database":[["Python and Pandas with Sentiment Analysis Database","/python-and-pandas-for-sentiment-analysis-and-finance/"],
                                                                        ["Pandas Basics","/pandas-basics-sentiment/"],
                                                                        ["Looking at our Data","/sentiment-analysis-data/"],
                                                                        ["Data Manipulation","/simple-data-manipulation/"],
                                                                        ["Removing Outlier Plots","/removing-outliers-sentiment/"],
                                                                        ["Basics for a Strategy","/simple-strategy-idea/"],
                                                                        ["Dynamic Moving Averages","/dynamic-moving-averages/"],
                                                                        ["Strategy Function","/strategy-function-tutorial/"],
                                                                        ["Mapping function to dataframe","/mapping-function-pandas-sentiment/"],
                                                                        ["Beginning to back-test","/back-testing-basics-sentiment/"],
                                                                        ["More Analysis","/more-analysis-sentiment/"],
                                                                        ["Conclusion","/sentiment-conclusion/"],],

                  "Creating a Monte Carlo simulator":[["Monte Carlo Introduction","/monte-carlo-simulator-python/"],
                                                      ["Monte Carlo dice Function","/monte-carlo-dice-function/"],
                                                      ["Creating a simple Bettor","/simple-bettor/"],
                                                      ["Plotting Results with Matpltolib","/plotting-monte-carlo-matplotlib/"],
                                                      ["Martingale Strategy","/martingale-strategy/"],
                                                      ["Bettor Statistics","/bettor-statistics-monte-carlo/"],
                                                      ["More comparison","/more-monte-carlo-comparison/"],
                                                      ["Graphing Monte Carlo","/graphing-monte-carlo/"],
                                                      ["Fixing Debt Issues","/fixing-debt-issues-monte-carlo/"],
                                                      ["Analyzing Monte Carlo results","/analyzing-monte-carlo-results/"],
                                                      ["Using Monte Carlo to find Best multiple","/using-monte-carlo-to-snoop/"],
                                                      ["Checking betting results","/checking-bettor-results/"],
                                                      ["D'Alembert Strategy","/dalembert-strategy/"],
                                                      ["50/50 Odds","/50-50-odds/"],
                                                      ["Analysis of D'Alembert","/dalembert-analysis/"],
                                                      ["Comparing Profitability","/comparing-profitability/"],
                                                      ["Finding best D'Alembert Multiple","/snooping-best-dalembert-multiple/"],
                                                      ["Two dimensional charting monte carlo","/two-dimension-graph-monte-carlo/"],
                                                      ["Monte Carlo Simulation and Python","/monte-carlo-python/"],
                                                      ["Labouchere System for Gambling Tested","/testing-labouchere/"],],

                  "IBpy":[["IBPy Tutorial for using Interactive Brokers API with Python","/ibpy-tutorial-using-interactive-brokers-api-python/"],],

                  "Programming for Fundamental Investing":[["Programming for Fundamental Investing","/python-fundamental-investing/"],
                                                           ["Getting Company Data","/fundamental-company-data/"],
                                                           ["Price to Book ratio example","/price-to-book-ratio/"],
                                                           ["Python Stock Screener for Price to Book","/create-a-stock-screener-python/"],
                                                           ["Python Screener for PEG Ratio","/peg-ratio-stock-screener/"],
                                                           ["Adding Price to Earnings","/price-to-earnings-screener/"],
                                                           ["Getting all Russell 3000 stock tickers","/compiling-russell-3000-tickers/"],
                                                           ["Getting all Russell 3000 stock tickers part 2","/compiling-russell-3000-tickers-2/"],
                                                           ["More stock Screening","/more-stock-screening/"],
                                                           ["Completing Basic Stock Screener","/completing-basic-stock-screener/"],
                                                           ["Connecting with Quandl for Annual Earnings Data","/connecting-with-quandl/"],
                                                           ["Organizing Earnings Data","/organizing-earnings-data/"],
                                                           ["Graphing Finance Data","/graphing-finance-data-fundamentals/"],
                                                           ["Finishing the Graphing","/finishing-fundamental-graphing/"],
                                                           ["Adding the Graphing to the Screener","/incorporating-graphing-into-stock-screener/"],
                                                           ["Preparing figure to Accept Finance Data","/preparing-figure-for-finance-data/"],
                                                           ["Adding Historical Earnings to Stock Screener Chart Data","/adding-historical-earnings/"],
                                                           ["Completing the Fundamental Investing Stock Screeners","/fundamental-investing-stock-screener-conclusion/"],],

                  "Virtual Private Server Basics":[["VPS with AWS EC2 and Python intro","/python-vps-intro/"],
                                                   ["Navigating the Terminal","/navigating-terminal/"],
                                                   ["Navigating the Terminal p.2","/terminal-navigation/"],
                                                   ["Crontab tutorial for cron jobs","/cron-tutorial-vps/"],
                                                   ["Running Multiple Scripts at Once","/running-multiple-scripts/"],
                                                   ["Using nohup command to Keep Scripts Alive","/nohup-command/"],
                                                   ["Python Anywhere using PythonAnywhere","/python-anywhere/"],],

                  "Practical Flask Creating PythonProgrammingnet":[["Introduction to Practical Flask","/practical-flask-introduction/"],
                                                                     ["Basic Flask Website tutorial","/basic-flask-website-tutorial/"],
                                                                     ["Flask with Bootstrap and Jinja Templating","/bootstrap-jinja-templates-flask/"],
                                                                     ["Starting our Website home page","/website-home-page-flask/"],
                                                                     ["Improving the Home Page","/flask-homepage-improvements/"],
                                                                     ["Finishing the Home Page","/flask-homepage-completed/"],
                                                                     ["Dynamic User Dashboard","/flask-user-dashboard/"],
                                                                     ["Content Management Beginnings","/flask-content-management-basics/"],
                                                                     ["Error Handling","/flask-error-handling-basics/"],
                                                                     ["Flask Flash function","/flash-flask-tutorial/"],
                                                                     ["Users with Flask intro","/flask-users-tutorial/"],
                                                                     ["Handling POST and GET Requests with Flask","/flask-get-post-requests-handling-tutorial/"],
                                                                     ["Creating MySQL database and table","/mysql-database-with-flask-tutorial/"],
                                                                     ["Connecting to MySQL database with MySQLdb","/flask-connect-mysql-using-mysqldb-tutorial/"],
                                                                     ["User Registration Form","/flask-user-registration-form-tutorial/"],
                                                                     ["Registration Code","/flask-registration-tutorial/"],
                                                                     ["Finishing User Registration","/flask-user-register-tutorial/"],
                                                                     ["Password Hashing with Flask Tutorial","/password-hashing-flask-tutorial/"],
                                                                     ["User Login System","/flask-user-log-in-system-tutorial/"],
                                                                     ["Decorators - Login_Required pages","/decorator-wrappers-flask-tutorial-login-required/"],
                                                                     ["Dynamic user-based content","/dynamic-user-based-content-flask-tutorial/"],
                                                                     ["More on Content Management","/flask-content-management-contd/"],
                                                                     ["Practical Flask Conclusion","/flask-conclusion-practical/"],

                                                                     ],

                  
                  

                  
                            }


    return TOPIC_DICT








if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])
