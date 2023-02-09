/*  Name: Matthew Nale
 *  Date of Last Edit: 2/9/2023
 *  
 *  Purpose: Calculate Ramp Up time Sub Metric of a given Github Repository
 *
 *  Details: Using provided data, calculates the Ramp Up time in the range of [0,1], with 1 being the quickest ramp up time and 0 the slowest
*/

use std::env;

//calculate_readme will return a weighting for the ramp up time, based on the size of the readme and the average number of comments per file
pub fn calculate_readme(readme_size: f64) -> f64{
    //Compare length of readme_file to base case value
    println!("Calculating README size");
    return 1.0
}

fn main() {
    let args : Vec<String> = env::args().collect();                         //Collects the argv values into a vector called args
    let readme_size : f64 = args[1].parse().unwrap();                       //Converts the string values into a f64 value 
    let num_comments : f64 = args[2].parse().unwrap();

    let readme_weight = calculate_readme(readme_size);
    println!("README size weighting: {readme_weight}");
}