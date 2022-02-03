

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

############################################## Class Rectanglr ############################################
class Rectangle(Point):
    def __init__(self, p1, p2, color):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.p1 = p1 
        self.p2 = p2  
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top = max(p1.y, p2.y)
        self.color = color
        #print ('\nInitializing Rectangle object') 


    def __repr__(self):
        '''(Point)->str
        Returns rectangle representation of Points p1 and p2'''
        return 'Rectangle('+str(self.p1)+','+str(self.p2)+',\''+self.color+'\')'
        #return 'Point('+str(self.p1.x)+','+str(self.p1.y)+')'
    
    def __str__(self):
        '''(Point)->str
        Explains the color, bottom left and top right points of a rectangle with canonical string representation of the points.'''
        return 'I am a ' + str(self.get_color()) + ' rectangle with bottom left corner at '+ str(self.p1) + ' and top right corner at ' + str(self.p2) + '.'

    def __eq__(self, r2):
        '''(Point,Point)->bool
        Returns True if self and other have the same points''' 
        #print('\n----------in eq r2=',r2)
        return self.p1 == r2.p1 and self.p2 == r2.p2

    def on_left_of(self, r2):
        '''(Point,Point)->bool
        Returns True if self and other have the same points''' 
        #print('\n----------in eq r2=',r2)
        return self.p1.x < r2.p1.x 

    def on_top_of(self, r2):
        '''(Point,Point)->bool
        Returns True if self and other have the same points''' 
        #print('\n----------in eq r2=',r2)
        return self.p2.y > r2.p2.y

    def get_width(self):
        return (self.p2.x - self.p1.x)
        
    def get_height(self):
        return (self.p2.y - self.p1.y)
          
    def get_bottom_left(self):
        #print ('\ncalling get_bottom_left')
        return (str(self.p1))

    def get_top_right(self): 
        #print ('\ncalling get_top_right')        
        return (str(self.p2))
         
    def get_color(self):
        #print ('\ncalling get_color')        
        return  self.color 
        
    def reset_color(self, newColor):
        #print ('\ncalling reset_color')
        self.color = newColor

    def get_perimeter(self):
        #print ('\ncalling get_perimeter')
        return (self.get_width() + self.get_height()) * 2

    def get_area(self):
        #print ('\ncalling get_area')         
        return (self.get_width() * self.get_height())
    
    def move(self, dx, dy):
        #print ('\ncalling move')
        self.p1.x = dx
        self.p1.y = dy
        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y + dy

    def intersects(self, r2):
        #print ('\ncalling intersects')         
        if (self.left > r2.right or self.right < r2.left) or (self.top < r2.bottom or self.bottom > r2.top):
            return False
        else:
            return True 
        
    def contains(self, x, y):
        #print ('\ncalling contains')        
        if (x >= self.left and x <= self.right) and (y >= self.bottom and y <= self.top):
            return True
        else:
            return False
 


############################################## Class Canvas ############################################
      
class Canvas(Rectangle):
    def __init__(self):
        '''
        () --> None
        Initialize canvas to an empty list.
        '''
        self.canvas = list()

    def __len__(self):
        '''
        () --> None
        Initialize canvas to an empty list.
        '''
        return len(self.canvas)
        
    def add_one_rectangle(self, r):
        '''
        () --> None
        Adds the given rectangle r the canvas.
        '''
        self.canvas.append(r)

    def count_same_color(self, color):
        '''
        () --> None
        Returns the count of the given color of a rectangles in tha canvas.
        '''
        if len(self.canvas) == 0:
            print('The canvas is empty.')
            return
        
        count = 0 
        for r in self.canvas:

            #print('\n---------------------Type(r)=',type(r))
            
            if r.get_color() == color:
                count += 1
        return count
    
    def get_rect(self, i):
        '''
        (int) ---> rec
        Returns a rectangle at index i of the canvas list.
        If canvas is empty, returns None
        '''
        return self.canvas[i]
        
    def total_perimeter(self):
        '''
        () --> int
        Calculates the sum of the perimiters of all rectangles in the canvas
        '''
        if len(self.canvas) == 0:
            print('\nThe canvas is empty.')
            return 0
        
        totalPerimiter = 0
        for rec in self.canvas:
            totalPerimiter += rec.get_perimeter()
        return totalPerimiter
              
    def min_enclosing_rectangle(self):
        '''
        () --> rec
        Creates and returns a smallest rectangle r with such bottom_left and top_right points that contains all rectangles in the canvas.
        Finds the bottom_left point of the left most rectangle and the top_right of the right most rectangle, adds one to the x and y coordinates
        of the fond points to create the new rectangle.
        '''
        if len(self.canvas) == 0:
            print('\nThe canvas is empty.')
            return Rectangle(Point(0,0), Point(0,0), 'Black')

        #Find the left most and top most rectangles
        leftMost_rec = self.canvas[0]
        bottomMost_rec = self.canvas[0]
        rightMost_rec = self.canvas[0]
        topMost_rec = self.canvas[0] 
        for i in range(1, len(self.canvas)):           
            if self.canvas[i].left < leftMost_rec.left:
                leftMost_rec = self.canvas[i]
            if self.canvas[i].bottom < bottomMost_rec.left:
                bottomMost_rec = self.canvas[i]
                
            if self.canvas[i].top > topMost_rec.top:
                topMost_rec = self.canvas[i]
            if self.canvas[i].right > rightMost_rec.top:
                rightMost_rec = self.canvas[i]
        print(Rectangle(Point(leftMost_rec.p1.x, bottomMost_rec.p1.y), Point(rightMost_rec.p2.x, topMost_rec.p2.y), 'Yellow').__repr__())


    def getAllPair_recs(self):
        '''
        () --> topple
        returns all subsets of size 2 of the rectangles in tha calling canvas.
        '''
        import itertools
        return list(itertools.combinations(self.canvas,2))        
        
    def common_point(self):
        '''
        () --> Boolean
        Returns True if there exists a point that intersects all rectangles in the calling canvas.
        Gets all pair rectangles and returns true if all pairs intersect.
        '''
        
        for pair_recs in self.getAllPair_recs():
            if pair_recs[0].intersects(pair_recs[1]) == False:
                return False
        return True


    def __repr__(self):
        '''(Point)->str
        Returns rectangle representation of Points p1 and p2'''
        return 'canvas(' + str(self.canvas) + ').'
    
    def __str__(self):
        '''(Point)->str
        Explains the color, bottom left and top right points of a rectangle with canonical string representation of the points.'''
        return 'canvas(' + str(self.canvas) + ').'



    
                    
#-------------------------------------------------------- sum_of_digits --------------------------------------------------------
def sum_of_digits(n):
   
    if (n == 0):
        return 0  
    else:
        return (n % 10) + sum_of_digits(n // 10)

def digital_root(n) :

    if len(str(n))==1:
        return n
    else:
        return digital_root(sum_of_digits(n))

