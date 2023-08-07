type point = [number, number, number]; // (x, y, z, ?w) 
type vertices = point[];

interface shape {
    type: "face" | "line"
    vertices: vertices
}