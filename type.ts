/* a point has a corresponding coordination 
   that has 3 (x, y, z) or 4 (x, y, z, w) value.*/
type point = [number, number, number];

/* a combination of vertices 
   composes a shape according to shape's mode.*/
type vertices = point[];

/* interface 'shape' defines the expressive type of a vertex combination.
   supports "face", "line".*/
interface shape {
    type: "face" | "line"
    vertices: vertices
}