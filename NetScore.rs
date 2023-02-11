/*  Name: Matthew Nale
 *  Date of Last Edit: 2/11/2023
 *
 *  Purpose: Calculate Net Score of a given Repository 
 *
 *  Details: Language not set, revamp file in new language if needed
 *      Calculates Net Score based on the given Metrics with appropriate weights
*/

use std::env;

//TODO This is a way to import Rust modules into other Rust files. License.py is excluded due to weird interactions due to Python
#[path = "NetScoreCalculation/MetricCalculation/Correctness.rs"] mod Correctness;
#[path = "NetScoreCalculation/MetricCalculation/RampUp.rs"] mod RampUp;
#[path = "NetScoreCalculation/MetricCalculation/BusFactor.rs"] mod BusFactor;
#[path = "NetScoreCalculation/MetricCalculation/Responsiveness.rs"] mod Responsiveness;


//*Main file used for testing. Compile command rustc needs a main function as well, due to not being able to compile libraries
//*Compile NetScore.rs with the 'rustc NetScore.rs' command, and run the executable with 3 args (open issues, closed issues, users).


//? Uncomment this block to test the Correctness.rs function. Takes 2 argv values (open issues, total stars)
/*
fn main() {
    let args : Vec<String> = env::args().collect();                                     //Collects the argv values into a vector called args
    let open : f64 = args[1].parse().unwrap();                                          //Converst the string values into a i32 value 
    let stars : f64 = args[2].parse().unwrap();
    let correct_base = Correctness::calculate_correctness(open, stars);                 //Calls the calculate_percentage to find the correctiveness base value
    println!("Base Correctness Weighting is: {correct_base}");
}*/

//? Uncomment this block to test the RampUp.rs function. Takes 2 argv values (readme size, average comments per file)
/*
fn main() {
    let args : Vec<String> = env::args().collect();                                     //Collects the argv values into a vector called args
    let readme_size : f64 = args[1].parse().unwrap();                                   //Converst the string values into a i32 value 
    let num_comments : f64 = args[2].parse().unwrap();
    let readme_weight = RampUp::calculate_readme(readme_size);
    println!("README size weighting: {readme_weight}");
}*/

//? Used for overall NetScore function
//* Args for this main are (num open issues, num stars, readme length (lines), num of comments)
fn main() {
    let args : Vec<String> = env::args().collect();
    let open_issues : f64 = args[1].parse().unwrap();
    let stars : f64 = args[2].parse().unwrap();
    let readme_size : f64 = args[3].parse().unwrap();
    let num_comments : f64 = args[4].parse().unwrap();

    let correctness_base : f64 = Correctness::calculate_correctness(open_issues, stars);
    let rampup_weight : f64 = RampUp::calculate_readme(readme_size);

    println!("Base Correctness Weighting is: {correctness_base}");
    println!("Base RampUp Weighting is: {rampup_weight}");
}