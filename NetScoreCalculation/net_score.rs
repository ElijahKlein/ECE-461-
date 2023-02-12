/*  Name:Matthew Nale
 *  Date of Last Edit: 2/12/2023
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
    let license_base : f64 = args[1].parse().unwrap();
    let open : f64 = args[2].parse().unwrap();                                          //Converst the string values into a f64 value for all args 
    let users : f64 = args[3].parse().unwrap();
    let readme_length : f64 = args[4].parse().unwrap();
    let last_pull : f64 = args[5].parse().unwrap();
    let pull_frequency : f64 = args[6].parse().unwrap();
    let repo_size : f64 = args[7].parse().unwrap();
    let num_contributors : f64 = args[8].parse().unwrap();

    let correct_base : f64 = correctness::calculate_correctness(open, users);                 //Calls the calculate_percentage to find the correctiveness base value
    let ramp_base : f64 = ramp_up::calculate_rampup(readme_length);
    let response_base : f64 = responsiveness::calculate_response(last_pull, pull_frequency, repo_size, num_contributors);
    let bus_base : f64 = 0.0;

    let mut net_score : f64 = ((5.0 * bus_base) + (4.0 * response_base) + (3.0 * correct_base) + (2.0 * ramp_base) + license_base) / 15.0;
    net_score = f64::trunc(net_score * 100.0) / 100.0;
    print!("{net_score} {correct_base} {ramp_base} {response_base} {bus_base} {license_base}");
}