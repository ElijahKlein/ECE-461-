 /*  Name: Matthew Nale
  *  Date of Last Edit: 2/8/2023
  *
  *  Purpose: Calculate Correctness Metric of a given Github Repository
  * 
  *  Details: Will perform calculations to determine the value of correctness of the given repository. This is done by analyzing
  *  the closed and open issues, in order to formulate a percentage value.
 */

use std::env;

//calculate_percentage will calculate the 70/30 split for open
pub fn calculate_percentage(open: f64, closed: f64, users: f64) {       
    //Grabs the ratio of open/closed issues to users
    let mut open_value : f64 = open / users;
    let mut closed_value : f64 = closed / users;

    //Applies the 70/30 weighting for values
    open_value = open_value * 0.7;
    closed_value = closed_value * 0.3;
    let total_weighting : f64 = 1.0 - (open_value + closed_value);
    println!("{total_weighting}");
}


//Main file used for testing. Compile command rustc needs a main function as well, due to not being able to compile libraries
fn main() {
    let args : Vec<String> = env::args().collect();                 //Collects the argv values into a vector called args
    let open : f64 = args[1].parse().unwrap();                      //Converst the string values into a i32 value 
    let closed : f64 = args[2].parse().unwrap();
    let users : f64 = args[3].parse().unwrap();
    calculate_percentage(open, closed, users);                      //Calls the calculate_percentage to find the correctiveness base value
}
