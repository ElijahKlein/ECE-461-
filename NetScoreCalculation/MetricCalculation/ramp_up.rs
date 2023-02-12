/*  Name: Matthew Nale
 *  Date of Last Edit: 2/12/2023
 *  
 *  Purpose: Calculate Ramp Up time Sub Metric of a given Github Repository
 *
 *  Details: Using provided data, calculates the Ramp Up time in the range of [0,1], with 1 being the quickest ramp up time and 0 the slowest
*/
use std::env;

//calculate_readme will return a weighting for the ramp up time, based on the size of the readme
pub fn calculate_rampup(readme_size: f64) -> f64{
    //Compare length of readme_file to base case value
    if readme_size <= 25.0 {
        return 0.0;
    }
    else if readme_size <= 50.0 {
        return 0.1;
    }
    else if readme_size <= 100.0 {
        return 0.2;
    }
    else if readme_size <= 200.0 {
        return 0.3;
    }
    else if readme_size <= 300.0 {
        return 0.4;
    }
    else if readme_size <= 400.0 {
        return 0.5;
    }
    else if readme_size <= 500.0 {
        return 0.6;
    }
    else if readme_size <= 600.0 {
        return 0.7;
    }
    else if readme_size <= 700.0 {
        return 0.8;
    }
    else if readme_size <= 800.0 {
        return 0.9;
    }
    else {
        return 1.0;
    }
}

fn main() {
    let args : Vec<String> = env::args().collect();                         //Collects the argv values into a vector called args
    let readme_size : f64 = args[1].parse().unwrap();                       //Converts the string values into a f64 value 

    let readme_weight = calculate_rampup(readme_size);
    println!("README size weighting: {readme_weight}");
}
