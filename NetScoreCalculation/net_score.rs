/*  Name:
 *  Date of Last Edit:
 *
 *  Purpose: Calculate Net Score of a given Repository 
 *
 *  Details: Language not set, revamp file in new language if needed
 *      Calculates Net Score based on the given Metrics with appropriate weights
*/

use std::env;

//TODO This is a way to import Rust modules into other Rust files. License.py is excluded due to weird interactions
#[path = "MetricCalculation/correctness.rs"] mod correctness;
#[path = "MetricCalculation/ramp_up.rs"] mod ramp_up;
#[path = "MetricCalculation/bus_factor.rs"] mod bus_factor;
#[path = "MetricCalculation/responsiveness.rs"] mod responsiveness;


//Main file used for testing. Compile command rustc needs a main function as well, due to not being able to compile libraries
//*Compile NetScore.rs with the 'rustc NetScore.rs' command, and run the executable with 3 args (open issues, closed issues, users).
fn main() {
    let args : Vec<String> = env::args().collect();                                     //Collects the argv values into a vector called args
    let open : f64 = args[1].parse().unwrap();                                          //Converst the string values into a i32 value 
    let closed : f64 = args[2].parse().unwrap();
    let users : f64 = args[3].parse().unwrap();
    let correct_base = correctness::calculate_percentage(open, closed, users);          //Calls the calculate_percentage to find the correctiveness base value
    println!("Base Correctness Weighting is: {correct_base}");
}