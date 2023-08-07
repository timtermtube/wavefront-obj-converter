/* a point has a corresponding coordination 
   that has 3 (x, y, z) or 4 (x, y, z, w) value.*/
type point = [number, number, number, number];

/* a combination of vertices 
   composes a shape according to shape's mode.*/
type vertices = point[];

/* interface 'shape' defines the expressive type of a vertex combination.
   supports "point", "line", "face".*/

/* if array 'vertices' provides invalid number of points,
   program terminates rendering a shape.
   as there are two points in "point" mode, or "face" mode, they are "invalid". */
interface shape {
    type: "point" | "face" | "line"
    vertices: vertices
}
/* 'complex' consists of shapes. */
interface complex {
    shapes: shape[]
}