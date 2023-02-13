 /*  Name: Matthew Nale
  *  Date of Last Edit: 2/12/2023
  *
  *  Purpose: Calculate Correctness Metric of a given Github Repository
  * 
  *  Details: Will perform calculations to determine the value of correctness of the given repository. This is done by analyzing
  *  the closed and open issues, in order to formulate a percentage value.
 */

use std::env;

//calculate_percentage will calculate the degree of correctness depending on open issues and number of stars
pub fn calculate_correctness(open: f64, stars: f64) -> f64{       
    //Grabs the ratio of open/total issues to users
    let total_weighting : f64 = open / stars;

    //* Yes, this is disgusting to look at. Couldn't be bothered to find an easier way lol. Plus easier to read/understand I guess
    if total_weighting  <= 0.0025{       //1 issue per 400 stars (1/0.0025)
        return 1.0;
    }
    else if total_weighting <= 0.005{    //1 issue per 200 stars (1/0.005)
        return 0.9;
    } 
    else if total_weighting <= 0.01{     //1 issue per 100 stars (1/0.01)
        return 0.8;
    }
    else if total_weighting <= 0.015{    //etc ...
        return 0.7;
    }
    else if total_weighting <= 0.02{
        return 0.6;
    }
    else if total_weighting <= 0.025{
        return 0.5;
    }
    else if total_weighting <= 0.03{
        return 0.4;
    }
    else if total_weighting <= 0.04{
        return 0.3;
    }
    else if total_weighting <= 0.05{
        return 0.2;
    }
    else if total_weighting <= 0.06{
        return 0.1;
    }
    else{
        return 0.0;
    }

}


//Main file used for testing. Compile command rustc needs a main function as well, due to not being able to compile libraries.
//Best to compile and use NetScore.rs instead. Used only for local testing
fn main() {
    let args : Vec<String> = env::args().collect();                         //Collects the argv values into a vector called args
    let open : f64 = args[1].parse().unwrap();                              //Converts the string values into a f64 value 
    let stars : f64 = args[2].parse().unwrap();
    let total_weighting = calculate_correctness(open, stars);               //Calls the calculate_percentage to find the correctiveness base value
    println!("Total weighting: {total_weighting}");
}
