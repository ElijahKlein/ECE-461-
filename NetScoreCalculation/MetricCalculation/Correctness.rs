 /*  Name: Matthew Nale
  *  Date of Last Edit: 2/8/2023
  *
  *  Purpose: Calculate Correctness Metric of a given Github Repository
  * 
  *  Details: Will perform calculations to determine the value of correctness of the given repository. This is done by analyzing
  *  the closed and open issues, in order to formulate a percentage value.
 */

use std::env;

//calculate_percentage will calculate the 70/30 split for open and total issues
pub fn calculate_percentage(open: f64, total: f64, users: f64) -> f64{       
    //Grabs the ratio of open/total issues to users
    let mut open_value : f64 = open / users;
    let mut total_value : f64 = total / users;

    //Applies the 70/30 weighting for values
    //TODO Weighting needs fixing. This below does not work correctly completely due to not knowing the users
    open_value = open_value * 0.7;
    total_value = total_value * 0.3;
    let mut total_weighting : f64 = 1.0 - (open_value + total_value);

    //TODO Binding between 0 and 1 values. This does not seem like a great idea however
    if total_weighting < 0.0 {
        total_weighting = 0.0;
        return total_weighting;
    }
    else if total_weighting > 1.0 {
        total_weighting = 1.0;
        return total_weighting;
    }
    else{
        return total_weighting;
    }
}


//Main file used for testing. Compile command rustc needs a main function as well, due to not being able to compile libraries.
//Best to compile and use NetScore.rs instead. Used only for local testing
fn main() {
    let args : Vec<String> = env::args().collect();                         //Collects the argv values into a vector called args
    let open : f64 = args[1].parse().unwrap();                              //Converts the string values into a i32 value 
    let closed : f64 = args[2].parse().unwrap();
    let users : f64 = args[3].parse().unwrap();
    let total_weighting = calculate_percentage(open, closed, users);        //Calls the calculate_percentage to find the correctiveness base value
    println!("{total_weighting}")
}
