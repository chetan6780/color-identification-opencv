# Importing required libraries
import pandas as pd
import cv2

# Function which gets the R,G,B values and return the most matching color name
# we will give values of R, G, B to the function i.e. value of red, green, blue color respectively to the function
# inside the function we will try to find minimum absolute difference in the values given and values present in our dataframe ,so that we can have almost accurate color values from which we can get color name.
def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R-int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B-int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            color_name = df.loc[i, 'color_name']
    return color_name

# Function which gives coordinates of mouse when clicked(Left mouse button down)
# when we click left button i.e. Left mouse button is pusshed down , this is a certen type of event in opencv known as EVENT_LBUTTONDOWN event.
# In our function if the event matches with EVENT_LBUTTONDOWN event we will get the r,g,b values of color and x,y cordinates of cursor,we chenge all of them globally so it will be accessible globally in program
def draw_function(event, x, y, flags, params):
    global clicked, r, g, b, xpos, ypos
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked, xpos, ypos = True, x, y
        b, g, r = list(map(int, img[y, x]))


# Path for image and csv file and reading the image
### Path for image and csv file and reading the image
# we will provide path for the input image and also for the csv file containing information about color then we will read the image and resize it such that we can see full image clearly.
img_path = r"C:\Users\Admin\Desktop\TSF\TASKS\2\imgs\img1.jpg"
csv_path = r"C:\Users\Admin\Desktop\TSF\TASKS\2\colors.csv"
img = cv2.imread(img_path)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# Creating the dataframe for colors csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)
# print(df.head(5))
# print(len(df))

# Creating window to display the image 
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_function)
clicked, r, g, b, xpos, ypos = False, 0, 0, 0, 0, 0

# In this, if we have clicked on the image we will create rectangle of identified color and then create a text to display information about detected color, if color is dark we will write text in white and color is very light we will write text in black color. After user click on ESC button the execution of program will stop and we will end the program by clearing all windows.
while True:
    cv2.imshow("Image", img)
    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness=-1) {-1 = fills entire rectangle }
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)

        # Creating the text for showing information
        text = get_color_name(r, g, b) + ' R:' + str(r) + ' G:' + str(g) + ' B:' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #  If the color is very light show the text in black color
        if r+g+b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
